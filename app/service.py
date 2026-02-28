"""Orchestrates preprocess -> agents -> compiler using depth rules."""

from __future__ import annotations

from typing import Any

from app.core.constants import STACK_FOLDER_TREES
from app.pipeline.agents import api_agent, code_agent, data_agent, perf_agent, ui_agent
from app.pipeline.compiler import compile_output
from app.pipeline.preprocess import preprocess_image, preprocess_video


def _folder_tree_for(stack_hint: str | None) -> str:
    if not stack_hint:
        return STACK_FOLDER_TREES["nextjs-fastapi"]
    key = stack_hint.strip().lower().replace(" + ", "-").replace(" ", "-")
    return STACK_FOLDER_TREES.get(key, STACK_FOLDER_TREES["nextjs-fastapi"])


def run_analysis(
    filename: str,
    mode: str,
    depth_level: int,
    stack_hint: str | None,
    duration_seconds: int = 0,
) -> dict[str, Any]:
    assumptions: list[str] = []
    folder_tree = _folder_tree_for(stack_hint)

    visual_parse = (
        preprocess_image(filename)
        if mode == "image"
        else preprocess_video(filename, duration_seconds=duration_seconds)
    )

    if "error" in visual_parse:
        assumptions.append(visual_parse["error"])

    ui_spec = ui_agent(visual_parse)

    db_spec: dict[str, Any] = {}
    api_spec: dict[str, Any] = {}
    if depth_level >= 2:
        db_spec = data_agent(visual_parse)
        api_spec = api_agent(db_spec)

    code_spec = code_agent(depth_level=depth_level, folder_tree=folder_tree)
    perf_spec = perf_agent(depth_level=depth_level)

    output = compile_output(ui_spec, db_spec, api_spec, code_spec, perf_spec, assumptions)
    return output.model_dump()
