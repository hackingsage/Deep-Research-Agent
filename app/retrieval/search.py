import httpx

async def search_duckduckgo(query: str):
    url = "https://duckduckgo.com/?q=" + query
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    return r.text[:4000]