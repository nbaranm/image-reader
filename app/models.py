"""Data models for request/response payloads."""

from __future__ import annotations

from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field, model_validator

from app.core.constants import SUPPORTED_DEPTHS, SUPPORTED_MODES


class AnalyzeRequest(BaseModel):
    mode: Literal["image", "video"]
    depth_level: int = Field(ge=1, le=3)
    stack_hint: str | None = None
    project_type: str | None = None

    @model_validator(mode="after")
    def validate_supported(self) -> "AnalyzeRequest":
        if self.mode not in SUPPORTED_MODES:
            raise ValueError("Unsupported mode")
        if self.depth_level not in SUPPORTED_DEPTHS:
            raise ValueError("Unsupported depth level")
        return self


class AnalyzeQueuedResponse(BaseModel):
    job_id: str = Field(default_factory=lambda: str(uuid4()))
    status: Literal["queued"] = "queued"


class AnalysisOutput(BaseModel):
    technical_summary: str
    confidence_score: int = Field(ge=0, le=100)
    assumptions: list[str]
    data_models: dict[str, Any]
    api_contract: dict[str, Any]
    frontend_structure: dict[str, Any]
    backend_structure: dict[str, Any]
    folder_tree: str
    code_snippets: dict[str, Any]
    optimization_notes: list[str]
