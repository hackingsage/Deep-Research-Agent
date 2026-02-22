from langgraph.graph import StateGraph
from typing import TypedDict
from .router import route_mode
from ..memory.qdrant_memory import search_memory, store_memory
from .self_reflection import self_reflect_node
from ..models.groq_client import generate_response

class AgentState(TypedDict):
    user_id: str
    query: str
    mode: str
    context: str
    answer: str


def router_node(state):
    state["mode"] = route_mode(state["query"])
    return state


def memory_node(state):
    memories = search_memory(state["query"], state["user_id"])
    state["context"] = "\n".join(
        [
            f"Previous research: {m.payload.get('summary','')}"
            for m in memories
        ]
    )
    return state


def reasoning_node(state):

    prompt = f"""
        You are a senior research engineer assistant.

        User context:
        {state['context']}

        Question:
        {state['query']}

        Mode: {state['mode']}

        Generate a structured technical report using EXACTLY this format:

        ## TL;DR
        (3-4 sentence summary)

        ## Core Concepts
        (clear explanation)

        ## Approaches / Methods
        (bullet comparison)

        ## Tradeoffs
        (pros, cons, performance implications)

        ## Production Recommendation
        (when an engineer should choose each)

        ## Example / Implementation Idea
        (optional code or system idea)

        Be precise and practical.
        """

    answer = generate_response(prompt)

    state["answer"] = answer
    return state

def memory_write_node(state):

    store_memory(
        state["user_id"],
        state["query"],
        {
            "type": "research_topic",
            "summary": state["answer"][:500]
        },
    )

    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router_node)
    graph.add_node("memory", memory_node)
    graph.add_node("reason", reasoning_node)
    graph.add_node("write_memory", memory_write_node)
    graph.add_node("self_reflect", self_reflect_node)

    graph.set_entry_point("router")

    graph.add_edge("router", "memory")
    graph.add_edge("memory", "reason")
    graph.add_edge("reason", "self_reflect")
    graph.add_edge("self_reflect", "write_memory")

    graph.set_finish_point("write_memory")

    return graph.compile()