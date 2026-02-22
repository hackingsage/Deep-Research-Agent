from fastapi import APIRouter
from ..agent.workflow import build_graph
from ..utils.metrics import start_timer, end_timer

router = APIRouter()
graph = build_graph()

@router.post("/research")
async def research(query: str, user_id: str = "default"):

    start = start_timer()

    result = graph.invoke({
        "query": query,
        "user_id": user_id,
        "mode": "",
        "context": "",
        "answer": "",
    })

    latency = end_timer(start)

    return {
        "answer": result["answer"],
        "mode": result["mode"],
        "latency_seconds": latency
    }