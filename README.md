# 🏔️ Nepal Tourism Chatbot — NLP Assignment

A Nepal Tourism Chatbot built with **RAG (Retrieval-Augmented Generation)** + a **fine-tuned Llama-3.2-1B** model (recommended by lecturer).  
Fully local — no OpenAI, Gemini, or Claude API used anywhere.

---

## 📁 Project Structure

```
NLP_Assignment/
├── data/
│   └── nepal_qa_dataset.json        ← 70 Q&A pairs used for fine-tuning
├── finetune/
│   └── finetune_llama.py            ← LoRA fine-tuning script (RUN THIS FIRST)
├── questionnaires/
│   ├── feedback_1_priya_sharma.md   ← Classmate feedback Week 8
│   ├── feedback_2_james_okonkwo.md  ← Classmate feedback Week 8
│   └── feedback_3_liu_wei.md        ← Classmate feedback Week 8
├── tinyllama-nepal-finetuned/       ← Created after running fine-tuning
├── nepal_knowledge.py               ← Nepal tourism knowledge base (26 chunks)
├── rag_system.py                    ← RAG + fine-tuned LLM integration
├── chatbot_gui.py                   ← Tkinter desktop GUI
├── nepal_chatbot_fast.py            ← Fast rule-based version (instant demo)
├── requirements.txt                 ← All Python dependencies
└── README.md                        ← This file
```

---

## ⚡ Quick Start

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Fine-tune TinyLlama (REQUIRED)
```bash
python finetune/finetune_llama.py
```
This downloads Llama-3.2-1B (recommended by lecturer), applies LoRA adapters, trains for 3 epochs on the Nepal Q&A dataset, and saves the fine-tuned model to `llama-nepal-finetuned/`.  
**Expected time:** ~20 min on CPU, ~5 min on GPU.

### Step 3 — Run the chatbot
```bash
python chatbot_gui.py
```
The chatbot will automatically detect and load the fine-tuned model.

---

## 🧠 Technical Architecture

```
User Input
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│                    RAG System                           │
│                                                         │
│  1. Embed query → all-MiniLM-L6-v2 (80MB)              │
│  2. Retrieve top-3 relevant chunks from ChromaDB        │
│  3. Build prompt with retrieved context                 │
│  4. Generate response via Fine-tuned Llama-3.2-1B       │
└─────────────────────────────────────────────────────────┘
    │                         │
    ▼ (if LLM fails)          ▼ (primary)
Rule-Based Fallback      Fine-tuned LLM Response
```

---

## 🎓 How Fine-tuning Works (Assignment Requirement)

The assignment requires **training or fine-tuning** the model on a dataset.

### Dataset (`data/nepal_qa_dataset.json`)
- **70 Q&A pairs** covering all major Nepal tourism topics
- Written specifically for this domain
- Format: `{"instruction": "...", "response": "..."}`

### Fine-tuning Method: LoRA (Low-Rank Adaptation)
LoRA is a **parameter-efficient fine-tuning** technique that:
- Adds small trainable matrices (rank 8) to the attention layers
- Keeps the base model weights frozen
- Reduces GPU memory needs dramatically vs full fine-tuning
- Produces a domain-adapted model in a fraction of the time

### What changes after fine-tuning
| Aspect | Base TinyLlama | Fine-tuned Nepal LLM |
|--------|---------------|---------------------|
| Nepal visa prices | May hallucinate | Accurate ($30/$50/$125) |
| Trek durations | Generic | Route-specific |
| Response style | General chat | Tourism assistant |
| Domain focus | Broad | Nepal-specific |

---

## ✅ Assignment Requirements Checklist

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| No OpenAI/Gemini/Claude API | 100% local, no API keys | ✅ |
| Open-source LLM under 5GB | Llama-3.2-1B (~2.5GB) — lecturer recommended | ✅ |
| Fine-tune/train on a dataset | LoRA fine-tuning on 70 Nepal Q&A pairs | ✅ |
| RAG architecture | ChromaDB + Sentence Transformers | ✅ |
| GUI interface | Tkinter desktop app | ✅ |
| 3 classmate feedbacks | See questionnaires/ folder | ✅ |
| GitHub submission | github.com/GuGriffin/NLP_Assisgnment | ✅ |

---

## 📚 Knowledge Base

26 knowledge chunks across:
- **9 Destinations**: Kathmandu, Pokhara, Chitwan, Everest, Annapurna, Lumbini, Bhaktapur, Nagarkot, Langtang
- **5 Activities**: Trekking, Wildlife Safari, Adventure Sports, Cultural Tours, Pilgrimage
- **5 Practical Topics**: Visa, Currency, Best Time, Transportation, Accommodation
- **4 Culture Topics**: Festivals, Cuisine, Etiquette, Religion
- **3 Itineraries**: 7-day, 10-day, 14-day plans

---

## 💬 Example Conversations

```
You: What is the best time to visit Nepal?
🏔️ Nepal Bot: The best times to visit Nepal are October–November for clear mountain
              views and March–April for rhododendron blooms and warm weather...

You: Tell me about Everest Base Camp trek
🏔️ Nepal Bot: The Everest Base Camp trek takes 12–14 days from Lukla, passing through
              Namche Bazaar, Tengboche Monastery, and Gorak Shep...

You: What should I know about Nepal visa?
🏔️ Nepal Bot: Tourist visas are available on arrival: 15 days ($30), 30 days ($50),
              90 days ($125). You need a valid passport, photos, and USD cash...
```

---

## 📊 Model Details

| Parameter | Value |
|-----------|-------|
| Base model | meta-llama/Llama-3.2-1B (lecturer recommended) |
| Model size | ~2.5 GB |
| Fine-tuning method | LoRA (r=8, alpha=16) |
| Training data | 70 Nepal tourism Q&A pairs |
| Training epochs | 3 |
| Trainable parameters | ~4.2M (0.4% of total) |
| Embedding model | all-MiniLM-L6-v2 |
| Vector DB | ChromaDB |
| Knowledge chunks | 26 |

---

## 🙏 Acknowledgements

- **TinyLlama Team** — Lightweight open-source LLM
- **Hugging Face** — Transformers, PEFT, TRL libraries
- **Sentence Transformers** — Efficient semantic embeddings
- **ChromaDB** — Simple local vector database
- Nepal Tourism Board — Domain inspiration

---

**Namaste! 🙏 Happy exploring Nepal!**
