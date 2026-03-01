from fastapi import APIRouter
from ..agent.workflow import build_graph
from ..utils.metrics import start_timer, end_timer
from pydantic import BaseModel

router = APIRouter()
graph = build_graph()

class ResearchRequest(BaseModel):
    query: str
    user_id: str = "default"

@router.post("/research")
async def research(req: ResearchRequest):

    query = req.query
    user_id = req.user_id

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
        "latency_seconds": latency,
        "memory_used": result.get("memory_used", [])
    }