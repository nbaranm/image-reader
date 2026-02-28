"""Celery task definitions for asynchronous V2T jobs."""

from celery import Celery

from app.service import run_analysis

celery_app = Celery("v2t", broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")


@celery_app.task(name="v2t.run_analysis")
def run_analysis_task(payload: dict) -> dict:
    return run_analysis(
        filename=payload.get("filename", "upload.bin"),
        mode=payload["mode"],
        depth_level=payload["depth_level"],
        stack_hint=payload.get("stack_hint"),
        duration_seconds=payload.get("duration_seconds", 0),
    )
