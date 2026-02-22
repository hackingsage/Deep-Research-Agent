# 🧠 Deep Research Engineer Agent

A production-style AI research agent that transforms technical questions into structured engineering insights using multi-stage reasoning, persistent memory, and adaptive model routing.

---

## 🚀 Features

- **Dual Research Modes** (Quick & Deep)
- **Persistent Semantic Memory** (Qdrant)
- **Self-Reflective Reasoning**
- **Structured Engineering Reports**
- **Multi-Model Fallback** (Quota Resilience)
- **Cost & Latency Tracking**
- **CPU-friendly local embeddings**

---

## 🏗 Architecture

```
User Query
    → Mode Router
    → Memory Retrieval (Qdrant)
    → Research Reasoning (LLM)
    → Self-Reflection Improvement
    → Persistent Memory Update
    → Structured Report
```

---

## 🧩 Tech Stack

- **LangGraph** (agent orchestration)
- **FastAPI** (API layer)
- **Qdrant** (vector memory)
- **Gemini API + Fallback LLM**
- **SentenceTransformers** (local embeddings)

---

## ⚡ Research Modes

### Quick Mode (<30s)
Fast high-signal technical explanations.

### Deep Mode (<3min)
Multi-step reasoning with tradeoff analysis.

---

## 🧠 Persistent Memory

The agent remembers:
- user preferences
- past research topics
- prior reports

Memory persists across sessions using semantic embeddings.

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Qdrant

```bash
docker compose up -d
```

### 3. Add API keys

Create `.env`:

```env
GROQ_API_KEY=your_key
```

## 4. Quick Start

```
docker compose up -d
python scripts/init_qdrant.py
uvicorn main:app --reload 
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## 📊 Example Query

```
Compare LoRA vs fine tuning tradeoffs
```

Produces structured engineering recommendations.