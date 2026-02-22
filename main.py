import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Deep Research Agent")

app.include_router(router)