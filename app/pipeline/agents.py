"""Deterministic multi-agent outputs from structured visual parse."""

from __future__ import annotations

from typing import Any


def ui_agent(visual_parse: dict[str, Any]) -> dict[str, Any]:
    return {
        "component_map": [],
        "layout_model": {"type": "unknown"},
        "accessibility_issues": [],
        "design_tokens": {},
        "evidence": visual_parse.get("evidence", []),
    }


def data_agent(visual_parse: dict[str, Any]) -> dict[str, Any]:
    return {
        "tables": [],
        "relationships": [],
        "sql": "-- No reliable entities detected from visual evidence",
        "evidence": visual_parse.get("evidence", []),
    }


def api_agent(data_spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "endpoints": [],
        "openapi_yaml": "openapi: 3.0.0\ninfo:\n  title: V2T Inferred API\n  version: 1.0.0\npaths: {}",
        "crud_mapping": {},
        "evidence": data_spec.get("evidence", []),
    }


def code_agent(depth_level: int, folder_tree: str) -> dict[str, Any]:
    frontend_files: dict[str, str] = {}
    backend_files: dict[str, str] = {}

    if depth_level >= 1:
        frontend_files["frontend/components/AppShell.tsx"] = "export default function AppShell(){return null;}"

    if depth_level >= 2:
        backend_files["backend/models/base.py"] = "class BaseModel: ..."

    if depth_level >= 3:
        backend_files["backend/main.py"] = "from fastapi import FastAPI\napp = FastAPI()"

    return {
        "folder_tree": folder_tree,
        "frontend_files": frontend_files,
        "backend_files": backend_files,
    }


def perf_agent(depth_level: int) -> dict[str, Any]:
    if depth_level < 3:
        return {
            "scalability_class": "low",
            "optimization_notes": ["Performance analysis enabled at depth_level=3."],
            "estimated_monthly_cost": {},
        }

    return {
        "scalability_class": "medium",
        "optimization_notes": [
            "Enable pagination for table-heavy routes.",
            "Cache stable list endpoints for 5 minutes.",
            "Add B-tree indexes on foreign keys and created_at.",
        ],
        "estimated_monthly_cost": {"tier": "starter", "usd": 80},
    }
