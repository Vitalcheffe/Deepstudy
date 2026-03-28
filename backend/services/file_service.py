"""
Deep Study AI — File Service
Handles file upload, storage, and text extraction.
"""

import os
import logging
import uuid
from typing import Optional

log = logging.getLogger(__name__)

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_upload(filename: str, content: bytes) -> str:
    """Save an uploaded file and return its ID."""
    file_id = str(uuid.uuid4())[:8]
    ext = os.path.splitext(filename)[1]
    path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")

    with open(path, "wb") as f:
        f.write(content)

    log.info("Saved upload: %s (%d bytes)", path, len(content))
    return file_id


def extract_text(file_id: str) -> str:
    """Extract text content from an uploaded file."""
    # Find the file
    for fname in os.listdir(UPLOAD_DIR):
        if fname.startswith(file_id):
            path = os.path.join(UPLOAD_DIR, fname)
            ext = os.path.splitext(fname)[1].lower()

            if ext == ".txt":
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()
            elif ext == ".pdf":
                try:
                    from PyPDF2 import PdfReader
                    reader = PdfReader(path)
                    return "\n".join(page.extract_text() or "" for page in reader.pages)
                except ImportError:
                    log.warning("PyPDF2 not installed, returning raw bytes")
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        return f.read()
            else:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()

    return ""


def delete_file(file_id: str) -> bool:
    """Delete an uploaded file."""
    for fname in os.listdir(UPLOAD_DIR):
        if fname.startswith(file_id):
            path = os.path.join(UPLOAD_DIR, fname)
            os.remove(path)
            log.info("Deleted: %s", path)
            return True
    return False
