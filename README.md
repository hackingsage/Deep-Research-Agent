# Deep Research Agent

A technical research assistant designed for engineering workflows.  
The system explores technical topics, retains research context across sessions, and produces structured reports focused on implementation tradeoffs rather than summaries.

This project was built for a hackathon challenge focused on production-ready AI agents.

---

## Overview

The agent answers technical questions using a multi-step workflow:

1. Classifies the query into quick or deep research mode
2. Retrieves relevant past context from persistent memory
3. Generates a structured technical analysis
4. Performs a self-review step to improve clarity and depth
5. Stores research context for future interactions

The goal is to simulate how a senior engineer researches unfamiliar technical topics — iteratively and with historical awareness.

---

## Key Features

- **Dual research modes**
  - Quick mode for focused explanations
  - Deep mode for comparative analysis and tradeoffs

- **Persistent semantic memory**
  - User preferences and prior research stored in Qdrant
  - Context reused across sessions

- **Structured technical outputs**
  - Reports emphasize tradeoffs, design decisions, and practical usage

- **Self-reflection step**
  - The agent reviews and refines its own response before returning results

- **Model fallback**
  - Automatically switches models when API quota limits are reached

- **Local embeddings**
  - CPU-friendly embeddings using SentenceTransformers

---

## Architecture

User Query
↓
Mode Router
↓
Memory Retrieval (Qdrant)
↓
LLM Reasoning
↓
Self-Reflection
↓
Memory Update
↓
Structured Response


### Components

| Component | Purpose |
|---|---|
| FastAPI | API interface |
| LangGraph | Agent workflow orchestration |
| Qdrant | Persistent vector memory |
| Gemini API | Primary reasoning model |
| Groq (fallback) | Reliability fallback model |
| SentenceTransformers | Local embedding generation |

---

## Research Modes

### Quick Mode
Designed for short technical explanations.

Target latency: **< 30 seconds**

### Deep Mode
Performs broader reasoning with comparisons and production considerations.

Target latency: **< 3 minutes**

---

## Memory Design

The system stores:

- user interaction preferences
- previously explored topics
- summarized research outputs

Memory retrieval is semantic rather than keyword-based, allowing follow-up queries such as:

> "Go deeper on the earlier report"

---

## Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Start Qdrant

```bash
docker compose up -d
```

### 3. Configure environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_key
```

### 4. Initialize vector memory (one time)

```bash
python init_memory.py
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Example Query

```
Compare LoRA vs fine tuning tradeoffs for production systems
```

The agent returns a structured engineering report including tradeoffs and recommendations.

---

## Design Goals

This project prioritizes:

* reliability over raw model performance
* reproducible setup
* persistent learning behavior
* clear system structure

The intention is to demonstrate how LLM agents can be organized as maintainable engineering systems rather than single prompts.

---

## Notes

* Embeddings run locally on CPU; no GPU required.
* Memory persists between restarts via Qdrant storage.
* The system includes automatic fallback handling when API limits are reached.

---

## License

MIT License