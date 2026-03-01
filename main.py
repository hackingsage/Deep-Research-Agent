import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from fastapi import FastAPI
from app.api.routes import router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Deep Research Agent")

app.include_router(router)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")