import json
import logging
import os

import azure.functions as func

logger = logging.getLogger(__name__)


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Health and config probe for the Digital Twin API (replace with real routes)."""
    body = {
        "status": "ok",
        "openai_endpoint_configured": bool(os.environ.get("AZURE_OPENAI_ENDPOINT")),
        "memory_container": os.environ.get("MEMORY_BLOB_CONTAINER", ""),
    }
    return func.HttpResponse(
        json.dumps(body),
        status_code=200,
        mimetype="application/json",
    )
