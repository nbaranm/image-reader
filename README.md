# V2T Analyzer (Vision-to-Task)

Production-ready scaffold implementing a deterministic V2T pipeline:

- FastAPI upload contract (`POST /analyze`)
- Async-ready Celery task entrypoint
- Preprocess + multi-agent analysis pipeline
- Strict output schema compiler
- Confidence and assumptions guardrails

## Run API

```bash
uvicorn app.main:app --reload
```

## Endpoints

- `POST /analyze`: queues a job and returns `{job_id, status:"queued"}`
- `POST /analyze/sync`: executes deterministic analysis and returns strict schema output

## Notes

- Video hard limit is 60 seconds.
- Confidence under 60 auto-adds `Structural ambiguity detected.`
- `depth_level` controls output breadth:
  - `1`: UI + folder structure
  - `2`: UI + DB + API
  - `3`: full stack + performance notes
