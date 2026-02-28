"""Project-wide constants for deterministic V2T output."""

OUTPUT_FLAG_STRUCTURAL_AMBIGUITY = "Structural ambiguity detected."
MAX_VIDEO_SECONDS = 60
MAX_IMAGE_EDGE = 1024
DEFAULT_MEDIA_TTL_HOURS = 24

SUPPORTED_MODES = {"image", "video"}
SUPPORTED_DEPTHS = {1, 2, 3}

DEFAULT_FOLDER_TREE = """/frontend
  /components
  /pages
  /hooks
  /styles
  /utils
/backend
  /api
  /models
  /schemas
  /services
  main.py
"""

STACK_FOLDER_TREES = {
    "nextjs-fastapi": DEFAULT_FOLDER_TREE,
    "react-node": """/frontend
  /src/components
  /src/pages
  /src/hooks
  /src/styles
/backend
  /src/routes
  /src/models
  /src/services
  server.js
""",
    "django": """/frontend
  /components
  /pages
/backend
  /project
  /apps
  manage.py
""",
    "supabase": """/frontend
  /components
  /pages
/supabase
  /functions
  /migrations
""",
    "cloudflare-workers": """/frontend
  /components
  /pages
/backend
  /workers
  wrangler.toml
""",
}
