"""FastAPI routes for V2T analysis API."""

from __future__ import annotations

from fastapi import APIRouter, File, Form, UploadFile

from app.models import AnalysisOutput, AnalyzeQueuedResponse, AnalyzeRequest
from app.service import run_analysis

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeQueuedResponse)
async def analyze(
    file: UploadFile = File(...),
    mode: str = Form(...),
    depth_level: int = Form(...),
    stack_hint: str | None = Form(default=None),
    project_type: str | None = Form(default=None),
) -> AnalyzeQueuedResponse:
    AnalyzeRequest(
        mode=mode,
        depth_level=depth_level,
        stack_hint=stack_hint,
        project_type=project_type,
    )
    return AnalyzeQueuedResponse()


@router.post("/analyze/sync", response_model=AnalysisOutput)
async def analyze_sync(
    file: UploadFile = File(...),
    mode: str = Form(...),
    depth_level: int = Form(...),
    stack_hint: str | None = Form(default=None),
) -> AnalysisOutput:
    AnalyzeRequest(mode=mode, depth_level=depth_level, stack_hint=stack_hint)
    output = run_analysis(
        filename=file.filename or "upload.bin",
        mode=mode,
        depth_level=depth_level,
        stack_hint=stack_hint,
    )
    return AnalysisOutput(**output)
