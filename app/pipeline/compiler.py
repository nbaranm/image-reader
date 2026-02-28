"""Spec compiler producing strict output schema payload."""

from __future__ import annotations

from typing import Any

from app.core.constants import OUTPUT_FLAG_STRUCTURAL_AMBIGUITY
from app.models import AnalysisOutput


def _calculate_confidence(assumptions: list[str], evidence_count: int) -> int:
    base = 90
    penalty = len(assumptions) * 8
    weak_evidence_penalty = 20 if evidence_count == 0 else 0
    score = max(0, min(100, base - penalty - weak_evidence_penalty))
    return score


def compile_output(
    ui_spec: dict[str, Any],
    db_spec: dict[str, Any],
    api_spec: dict[str, Any],
    code_spec: dict[str, Any],
    perf_spec: dict[str, Any],
    assumptions: list[str],
) -> AnalysisOutput:
    evidence_count = len(ui_spec.get("evidence", []))
    confidence = _calculate_confidence(assumptions, evidence_count)

    if confidence < 60 and OUTPUT_FLAG_STRUCTURAL_AMBIGUITY not in assumptions:
        assumptions.append(OUTPUT_FLAG_STRUCTURAL_AMBIGUITY)

    return AnalysisOutput(
        technical_summary="Deterministic V2T technical specification generated.",
        confidence_score=confidence,
        assumptions=assumptions,
        data_models=db_spec,
        api_contract=api_spec,
        frontend_structure={
            "component_map": ui_spec.get("component_map", []),
            "layout_model": ui_spec.get("layout_model", {}),
            "design_tokens": ui_spec.get("design_tokens", {}),
        },
        backend_structure={
            "services": [],
            "accessibility_issues": ui_spec.get("accessibility_issues", []),
            "scalability_class": perf_spec.get("scalability_class", "low"),
        },
        folder_tree=code_spec.get("folder_tree", ""),
        code_snippets={
            "frontend_files": code_spec.get("frontend_files", {}),
            "backend_files": code_spec.get("backend_files", {}),
        },
        optimization_notes=perf_spec.get("optimization_notes", []),
    )
