"""
RAG System for Nepal Tourism Chatbot
Combines vector search with a FINE-TUNED local LLM for accurate question answering.
No external API dependencies — fully local implementation.

IMPORTANT: Run finetune/finetune_tinyllama.py first to create the fine-tuned model.
If the fine-tuned model is not found, the system falls back to the base model.
"""

import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from nepal_knowledge import get_knowledge_chunks, NEPAL_TOURISM_DATA
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────────────────
BASE_DIR          = os.path.dirname(os.path.abspath(__file__))
FINETUNED_DIR     = os.path.join(BASE_DIR, "llama-nepal-finetuned")
BASE_MODEL_NAME   = "meta-llama/Llama-3.2-1B"
FINETUNED_MARKER  = os.path.join(FINETUNED_DIR, "FINETUNED_MARKER.txt")


def _model_to_load() -> tuple[str, bool]:
    """Return (model_path_or_name, is_finetuned)."""
    if os.path.isfile(FINETUNED_MARKER):
        print(f"[✓] Fine-tuned model found at: {FINETUNED_DIR}")
        return FINETUNED_DIR, True
    print(f"[!] Fine-tuned model NOT found. Using base model: {BASE_MODEL_NAME}")
    print("    → Run  python finetune/finetune_tinyllama.py  to fine-tune first.")
    return BASE_MODEL_NAME, False


# ─────────────────────────────────────────────────────────
# RAG System
# ─────────────────────────────────────────────────────────

class NepalTourismRAG:
    def __init__(self):
        print("Initializing Nepal Tourism RAG System…")

        # ── Vector store ──────────────────────────────────
        self.client = chromadb.Client(Settings(
            anonymized_telemetry=False,
            allow_reset=True,
            is_persistent=False,
        ))
        try:
            self.collection = self.client.get_collection("nepal_tourism")
            print("[✓] Loaded existing knowledge base")
        except Exception:
            self.collection = self.client.create_collection("nepal_tourism")
            print("[·] Creating new knowledge base…")
            self._build_knowledge_base()

        # ── Embedding model ───────────────────────────────
        print("[·] Loading embedding model (all-MiniLM-L6-v2)…")
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        # ── LLM (fine-tuned preferred) ────────────────────
        model_path, self.is_finetuned = _model_to_load()
        model_label = "Fine-tuned Nepal LLM" if self.is_finetuned else "Base TinyLlama-1.1B"
        print(f"[·] Loading {model_label}…")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.llm = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float32,
            device_map="auto",
            trust_remote_code=True,
        )
        self.llm.eval()
        status = "FINE-TUNED ✓" if self.is_finetuned else "base (not fine-tuned)"
        print(f"[✓] RAG System ready — LLM: {status}")

    # ── Knowledge base ────────────────────────────────────

    def _build_knowledge_base(self):
        chunks = get_knowledge_chunks()
        docs, metas, ids = [], [], []
        for i, chunk in enumerate(chunks):
            docs.append(chunk)
            metas.append({"source": "nepal_tourism", "chunk_id": i})
            ids.append(f"chunk_{i}")
        self.collection.add(documents=docs, metadatas=metas, ids=ids)
        print(f"[✓] Indexed {len(docs)} knowledge chunks")

    # ── Retrieval ─────────────────────────────────────────

    def _get_embedding(self, text: str):
        return self.embedding_model.encode(text).tolist()

    def retrieve_context(self, query: str, top_k: int = 3):
        results = self.collection.query(
            query_embeddings=[self._get_embedding(query)],
            n_results=top_k,
        )
        return results["documents"][0] if results and results["documents"] else []

    # ── Generation ────────────────────────────────────────

    def generate_response(self, query: str, context: list) -> str:
        context_text = "\n\n".join(context) if context else "No specific context available."

        # Use the same prompt format as fine-tuning
        prompt = (
            "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
            "You are a helpful Nepal Tourism Assistant. Use the provided context to answer "
            "questions about Nepal tourism accurately and helpfully.\n"
            "Context:\n"
            f"{context_text}<|eot_id|>"
            "<|start_header_id|>user<|end_header_id|>\n"
            f"{query}<|eot_id|>"
            "<|start_header_id|>assistant<|end_header_id|>\n"
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.llm.device)

        with torch.no_grad():
            outputs = self.llm.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=self.tokenizer.eos_token_id,
                repetition_penalty=1.1,
            )

        response = self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True,
        ).strip()

        # Clean up any prompt leakage
        for marker in ["<|eot_id|>", "<|start_header_id|>", "user", "system", "assistant"]:
            if marker in response:
                response = response.split(marker)[0].strip()

        return response

    # ── Public API ────────────────────────────────────────

    def query(self, question: str):
        print(f"\n[·] Processing: {question}")
        context  = self.retrieve_context(question)
        response = self.generate_response(question, context)
        return response, context


# ─────────────────────────────────────────────────────────
# Rule-based fallback (always available instantly)
# ─────────────────────────────────────────────────────────

def rule_based_response(query: str):
    q = query.lower()

    if any(w in q for w in ["hello", "hi", "namaste", "greet"]):
        return "Namaste! Welcome to Nepal Tourism Chatbot. I'm here to help you plan your perfect Nepal adventure. What would you like to know?", []
    if any(w in q for w in ["visa", "permission", "entry"]):
        return ("Tourist visas are available on arrival for most nationalities at Tribhuvan International Airport. "
                "Options: 15 days ($30), 30 days ($50), or 90 days ($125). You will need a valid passport "
                "(6 months validity), passport photos, completed form, and USD cash."), []
    if any(w in q for w in ["best time", "when to visit", "season"]):
        return ("The best times to visit Nepal are October–November (clear skies, best mountain views) "
                "and March–April (warmer weather, rhododendron blooms). Monsoon (Jun–Sep) is lush but wet; "
                "winter (Dec–Feb) is cold but clear and good for lower-altitude treks."), []
    if any(w in q for w in ["trek", "trekking", "hike", "hiking"]):
        return ("Nepal offers world-class trekking! Popular routes include Everest Base Camp (challenging, 12–14 days), "
                "Annapurna Circuit (moderate–challenging, 15–20 days), Langtang Valley (moderate, 7–10 days), "
                "and Ghorepani Poon Hill (easy, 4–5 days). A TIMS card and relevant permits are required."), []
    if any(w in q for w in ["pokhara", "lake", "paragliding"]):
        return ("Pokhara is Nepal's tourism capital, famous for Phewa Lake, stunning mountain views, and adventure activities. "
                "Must-see spots: Davis Fall, Gupteshwor Cave, World Peace Pagoda, Sarangkot sunrise, "
                "boating, paragliding, and zip-lining!"), []
    if any(w in q for w in ["everest", "base camp", "sagarmatha"]):
        return ("Mount Everest (8,848.86 m) is the world's highest peak! The Everest Base Camp trek takes 12–14 days, "
                "passing through Namche Bazaar and Tengboche Monastery. Best seasons: March–May and September–November. "
                "Helicopter tours are also available."), []
    if any(w in q for w in ["chitwan", "wildlife", "safari", "jungle"]):
        return ("Chitwan National Park is a UNESCO World Heritage Site famous for one-horned rhinoceros and Bengal tigers. "
                "Enjoy jungle safaris, bird watching, canoe rides on the Rapti River, and Tharu cultural shows. "
                "Best visited October–February."), []
    if any(w in q for w in ["lumbini", "buddha", "pilgrimage"]):
        return ("Lumbini is the birthplace of Lord Buddha and a major Buddhist pilgrimage site. Key attractions include "
                "Maya Devi Temple, Ashoka Pillar, Sacred Garden, and the Monastic Zone. Best visited October–April."), []
    if any(w in q for w in ["food", "cuisine", "eat", "dal bhat", "momo"]):
        return ("Must-try Nepali dishes: Dal Bhat (lentil soup with rice — the trekking staple), Momo (dumplings), "
                "Sel Roti (ring-shaped fried bread), Thukpa (Tibetan noodle soup). Newari cuisine is also incredible!"), []
    if any(w in q for w in ["kathmandu", "capital", "thamel"]):
        return ("Kathmandu, the 'City of Temples', has seven UNESCO World Heritage Sites! "
                "Don't miss Kathmandu Durbar Square, Swayambhunath (Monkey Temple), Boudhanath Stupa, "
                "and Pashupatinath Temple. Thamel is the tourist hub."), []
    if any(w in q for w in ["itinerary", "plan", "schedule", "days"]):
        return ("For a first visit consider: 7 days (Kathmandu + Pokhara highlights), 10 days (add Chitwan safari), "
                "or 14 days (complete experience including Lumbini). Peak season bookings should be made in advance."), []
    if any(w in q for w in ["cost", "budget", "expensive", "cheap", "money", "currency"]):
        return ("Nepal uses Nepalese Rupee (NPR), approx. 1 USD = 130–135 NPR. Budget: $25–40/day, "
                "mid-range: $50–100/day, luxury: $150+/day. ATMs available in cities; carry cash for remote areas."), []

    return None, []


# ─────────────────────────────────────────────────────────
# Chatbot controller
# ─────────────────────────────────────────────────────────

class NepalChatbot:
    def __init__(self):
        self.rag_system  = None
        self.initialized = False

    def initialize(self) -> bool:
        try:
            self.rag_system  = NepalTourismRAG()
            self.initialized = True
            return True
        except Exception as e:
            print(f"[!] Could not initialize full RAG system: {e}")
            print("    Using rule-based responses only.")
            return False

    def respond(self, query: str) -> str:
        if self.initialized and self.rag_system:
            try:
                response, _ = self.rag_system.query(query)
                if response and len(response) > 10:
                    return response
            except Exception as e:
                print(f"[!] LLM query failed: {e}")

        # Fallback
        response, _ = rule_based_response(query)
        if response:
            return response

        return ("I'd love to help with Nepal tourism! Ask me about destinations "
                "(Kathmandu, Pokhara, Everest, Chitwan, Lumbini), activities, visa requirements, "
                "best time to visit, food, culture, or itinerary planning. Namaste! 🙏")


# ─────────────────────────────────────────────────────────
# Standalone test
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    chatbot = NepalChatbot()
    chatbot.initialize()

    test_queries = [
        "What is the best time to visit Nepal?",
        "Tell me about trekking in Everest region",
        "What are the visa requirements for Nepal?",
    ]

    for q in test_queries:
        print("\n" + "=" * 60)
        print(f"Query: {q}")
        print(f"Response: {chatbot.respond(q)}")
        print("=" * 60)
