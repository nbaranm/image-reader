"""Media preprocessing and lightweight extraction stubs."""

from __future__ import annotations

from typing import Any

from app.core.constants import MAX_VIDEO_SECONDS


def preprocess_image(filename: str) -> dict[str, Any]:
    return {
        "mode": "image",
        "file": filename,
        "steps": ["resize_max_1024", "ocr", "color_clusters", "vision_parse"],
        "ui_elements": [],
        "text_blocks": [],
        "layout_description": "",
        "interaction_hints": [],
        "detected_errors": [],
        "evidence": [],
    }


def preprocess_video(filename: str, duration_seconds: int) -> dict[str, Any]:
    if duration_seconds > MAX_VIDEO_SECONDS:
        return {
            "error": "Video exceeds 60 seconds.",
            "mode": "video",
            "file": filename,
            "frames": [],
        }

    return {
        "mode": "video",
        "file": filename,
        "steps": [
            "sample_frames_every_2s",
            "deduplicate_ssim",
            "ocr_per_frame",
            "motion_detection",
            "transition_detection",
        ],
        "frames": [],
        "interaction_events": [],
        "state_transitions": [],
        "detected_routes": [],
        "evidence": [],
    }
