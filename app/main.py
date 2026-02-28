"""Application entrypoint."""

from fastapi import FastAPI

from app.api import router

app = FastAPI(title="V2T Analyzer", version="1.0.0")
app.include_router(router)
