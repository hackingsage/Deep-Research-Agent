def route_mode(query: str) -> str:
    deep_keywords = [
        "compare",
        "tradeoffs",
        "deep dive",
        "research",
        "benchmark",
        "detail",
        "design"
    ]

    if any(k in query.lower() for k in deep_keywords):
        return "deep"

    if len(query.split()) > 20:
        return "deep"

    return "quick"
