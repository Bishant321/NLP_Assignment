"""
Fine-tuning TinyLlama-1.1B on Nepal Tourism Q&A Dataset
Uses LoRA (Low-Rank Adaptation) for efficient parameter-efficient fine-tuning
This is the KEY script that meets the assignment requirement of training/fine-tuning

Run this BEFORE running the chatbot:
    pip install peft trl transformers torch datasets
    python finetune/finetune_tinyllama.py

Output: saves fine-tuned model to ../tinyllama-nepal-finetuned/
"""

import os
import json
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, TaskType, PeftModel
from trl import SFTTrainer, SFTConfig
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────
BASE_MODEL   = "meta-llama/Llama-3.2-1B"
DATA_PATH    = os.path.join(os.path.dirname(__file__), "..", "data", "nepal_qa_dataset.json")
OUTPUT_DIR   = os.path.join(os.path.dirname(__file__), "..", "llama-nepal-finetuned")
MAX_SEQ_LEN  = 512
NUM_EPOCHS   = 3
BATCH_SIZE   = 2           # keep small for low-VRAM / CPU training
LEARNING_RATE = 2e-4
LORA_R       = 8           # LoRA rank
LORA_ALPHA   = 16
LORA_DROPOUT = 0.05

# ─────────────────────────────────────────────────────────
# 1. LOAD & FORMAT DATASET
# ─────────────────────────────────────────────────────────

def load_dataset_from_json(path: str) -> Dataset:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    # Format each example as a single training string (Llama-3.2 format)
    formatted = []
    for item in raw:
        text = (
            f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
            f"You are a helpful Nepal Tourism Assistant.<|eot_id|>"
            f"<|start_header_id|>user<|end_header_id|>\n"
            f"{item['instruction']}<|eot_id|>"
            f"<|start_header_id|>assistant<|end_header_id|>\n"
            f"{item['response']}<|eot_id|>"
        )
        formatted.append({"text": text})

    dataset = Dataset.from_list(formatted)
    print(f"[✓] Loaded {len(dataset)} training examples from {path}")
    return dataset


# ─────────────────────────────────────────────────────────
# 2. LOAD TOKENIZER & BASE MODEL
# ─────────────────────────────────────────────────────────

def load_base_model():
    print(f"[·] Loading tokenizer: {BASE_MODEL}")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    print(f"[·] Loading base model: {BASE_MODEL} (Llama-3.2-1B)")
    # Use float32 for CPU; if you have a GPU with enough VRAM uncomment
    # the BitsAndBytesConfig lines below for 4-bit quantization (faster)
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.float16,
    # )
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float32,   # change to torch.float16 if GPU available
        device_map="cpu",
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        # quantization_config=bnb_config,  # uncomment for 4-bit GPU training
    )
    model.config.use_cache = False
    model.config.pretraining_tp = 1
    print("[✓] Base model loaded.")
    return model, tokenizer


# ─────────────────────────────────────────────────────────
# 3. APPLY LoRA ADAPTERS
# ─────────────────────────────────────────────────────────

def apply_lora(model):
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model


# ─────────────────────────────────────────────────────────
# 4. TRAIN
# ─────────────────────────────────────────────────────────

def train(model, tokenizer, dataset):
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=4,
        learning_rate=LEARNING_RATE,
        fp16=False,          # set True if using GPU
        bf16=False,
        logging_steps=10,
        save_strategy="epoch",
        optim="adamw_torch",
        warmup_ratio=0.05,
        lr_scheduler_type="cosine",
        report_to="none",    # disable wandb / tensorboard
        dataloader_num_workers=0,
        max_length=MAX_SEQ_LEN,
        dataset_text_field="text",
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
        formatting_func=lambda example: example["text"],
    )

    print("\n[·] Starting fine-tuning …")
    trainer.train()
    print("[✓] Training complete.")
    return trainer


# ─────────────────────────────────────────────────────────
# 5. SAVE FINE-TUNED MODEL
# ─────────────────────────────────────────────────────────

def save_model(trainer, tokenizer):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"[·] Saving fine-tuned model to {OUTPUT_DIR} …")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    # Save a marker file so rag_system.py knows the model is fine-tuned
    with open(os.path.join(OUTPUT_DIR, "FINETUNED_MARKER.txt"), "w") as f:
        f.write("This model has been fine-tuned on the Nepal Tourism Q&A dataset.\n")
        f.write(f"Base model: {BASE_MODEL}\n")
        f.write(f"Training examples: 70\n")
        f.write(f"Epochs: {NUM_EPOCHS}\n")
        f.write(f"LoRA rank: {LORA_R}\n")

    print(f"[✓] Model saved to: {OUTPUT_DIR}")


# ─────────────────────────────────────────────────────────
# 6. QUICK INFERENCE TEST
# ─────────────────────────────────────────────────────────

def test_model(model, tokenizer):
    print("\n[·] Running quick inference test …")
    test_questions = [
        "What is the best time to visit Nepal?",
        "Tell me about Everest Base Camp trek.",
    ]
    model.eval()
    for question in test_questions:
        prompt = (
            f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
            f"You are a helpful Nepal Tourism Assistant.<|eot_id|>"
            f"<|start_header_id|>user<|end_header_id|>\n"
            f"{question}<|eot_id|>"
            f"<|start_header_id|>assistant<|end_header_id|>\n"
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id,
            )
        response = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True,
        ).strip()
        print(f"\nQ: {question}")
        print(f"A: {response[:300]}")
    print("\n[✓] Inference test complete.")


# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print(" Nepal Tourism Chatbot — Llama-3.2-1B Fine-Tuning")
    print("=" * 60)
    print(f" Base model : {BASE_MODEL}")
    print(f" Data file  : {DATA_PATH}")
    print(f" Output dir : {OUTPUT_DIR}")
    print(f" Epochs     : {NUM_EPOCHS}  |  LoRA rank: {LORA_R}")
    print("=" * 60)

    # Check dependencies
    try:
        import peft, trl
        print("[✓] peft and trl are installed.")
    except ImportError:
        print("[✗] Missing dependencies. Run:")
        print("    pip install peft trl transformers torch datasets")
        exit(1)

    dataset       = load_dataset_from_json(DATA_PATH)
    model, tokenizer = load_base_model()
    model         = apply_lora(model)
    trainer       = train(model, tokenizer, dataset)
    save_model(trainer, tokenizer)
    test_model(trainer.model, tokenizer)

    print("\n" + "=" * 60)
    print(" Fine-tuning complete!")
    print(f" Fine-tuned model saved to: {OUTPUT_DIR}")
    print(" Now run the chatbot:  python chatbot_gui.py")
    print("=" * 60)
