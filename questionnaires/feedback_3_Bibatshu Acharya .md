# Nepal Tourism Chatbot — Usability Feedback Form
## Participant 3 | Week 8 Evaluation

---

**Evaluator Name:** Bibatshu Acharya  
**Date of Evaluation:** Week 8  
**Task:** Testing Nepal Tourism Chatbot (GUI version, full RAG mode)  
**Testing Environment:** Ubuntu 22.04, Python 3.10, NVIDIA GTX 1060 GPU  

---

## Section A — Ease of Use  
*Rate each item from 1 (Strongly Disagree) to 5 (Strongly Agree)*

| No. | Statement | Rating |
|-----|-----------|--------|
| 1 | The chatbot was easy to start and use | **5** |
| 2 | The interface buttons (Quick Questions) were helpful | **4** |
| 3 | I could understand what to type without instructions | **5** |
| 4 | The response time was acceptable | **5** |
| 5 | The chatbot gave relevant answers | **4** |

> *Note on Q4: With GPU, response times were around 3–5 seconds which is very good.*

---

## Section B — Content & Accuracy  
*Rate each item from 1 (Very Poor) to 5 (Excellent)*

| No. | Statement | Rating |
|-----|-----------|--------|
| 6 | Accuracy of visa information | **4** |
| 7 | Accuracy of trekking information | **5** |
| 8 | Usefulness of itinerary recommendations | **4** |
| 9 | Quality of food and culture responses | **5** |
| 10 | Overall helpfulness for Nepal travel planning | **5** |

---

## Section C — Open-ended Questions

**Q1: What did you like most about the chatbot?**  
> As a computer science student, I appreciate the technical architecture. The RAG system using ChromaDB with sentence transformers is a solid approach — it avoids hallucination by grounding responses in a knowledge base. The architecture diagram in the README is clear and professional. The fine-tuning on a custom Nepal dataset makes this genuinely better than just using the base model off the shelf.

**Q2: What was the most confusing or frustrating thing?**  
> Sometimes the fine-tuned model would give slightly longer responses than needed. A token length control slider in the UI would be useful. Also I noticed that when I asked in Chinese ("尼泊尔最好的时间是什么?"), it didn't understand — multilingual support would expand the audience significantly.

**Q3: Did the chatbot feel like it "understood" you?**  
> Yes, especially for trekking questions. I asked detailed questions about the Manaslu Circuit permits and it handled them correctly. The embedding-based retrieval means semantically similar questions get the right context even if I word it differently. That's exactly what RAG is supposed to do.

**Q4: Would you use this chatbot to plan a real Nepal trip?**  
> I would. I have been interested in the Everest Base Camp trek for a few years. I asked it 12 questions about the trek — permit costs, gear requirements, altitude sickness, teahouses, fitness requirements — and it answered all of them well. I would use it as my first research stop.

**Q5: Any suggestions for improvement?**  
> - Fine-tune on a larger dataset with 500+ examples for better generalization  
> - Add a confidence score display to show how certain the RAG retrieval is  
> - Consider deploying as a web app with Flask/FastAPI for easier sharing  
> - Add support for at least Mandarin and Hindi given Nepal's tourism demographics  
> - Persistent conversation history (memory) would make longer planning sessions better  
> - Consider RAG with reranking for better precision on niche questions  

---

## Section D — Overall Rating

| Metric | Score |
|--------|-------|
| Ease of Use | 4.7 / 5 |
| Content Quality | 4.6 / 5 |
| Interface Design | 4.3 / 5 |
| **Overall** | **4.5 / 5** |

---

*From a technical perspective, using LoRA fine-tuning + RAG is the right approach for a course project chatbot. It demonstrates real understanding of the NLP pipeline. The fine-tuning on domain-specific data is what separates this from a simple prompt-engineering project.*

*Signature: Bibatshu Acharya*
