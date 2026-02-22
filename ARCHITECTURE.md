# Architecture Overview

## System Flow

User Query
→ Mode Router
→ Qdrant Memory Retrieval
→ Research Reasoning (LLM)
→ Self-Reflection Improvement
→ Memory Persistence
→ Structured Report Output

## Components

### LangGraph Orchestrator
Controls deterministic multi-step reasoning.

### Qdrant Vector Database
Stores semantic research history and user preferences.

### Local Embeddings
SentenceTransformers provide CPU-friendly embeddings.

### Multi-Model Routing
Gemini used as primary model with automatic fallback.

## Design Goals

- Production reliability
- Persistent learning
- Cost-aware execution
- Structured engineering outputs