"""
Deep Study AI — Main FastAPI Application
"""

import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Firebase init
try:
    import firebase_admin
    from firebase_admin import credentials
    config_path = os.getenv("FIREBASE_CONFIG_PATH", "firebase_config.json")
    if os.path.exists(config_path):
        cred = credentials.Certificate(config_path)
        firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Firebase init skipped: {e}")

from services.ai_service import generate_summary, generate_quiz, generate_mindmap, is_available as ai_available
from services.file_service import save_upload, extract_text, delete_file
from services.auth_service import verify_token

app = FastAPI(title="Deep Study AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok", "ai": ai_available()}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file and extract its text content."""
    if not file.filename:
        raise HTTPException(400, "No filename provided")

    content = await file.read()
    if len(content) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(413, "File too large (max 10MB)")

    file_id = save_upload(file.filename, content)
    text = extract_text(file_id)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "text_length": len(text),
        "preview": text[:500] if text else "",
    }


@app.post("/summary/{file_id}")
async def get_summary(file_id: str):
    """Generate a summary from an uploaded file."""
    text = extract_text(file_id)
    if not text:
        raise HTTPException(404, "File not found or empty")

    summary = generate_summary(text)
    return {"file_id": file_id, "summary": summary}


@app.post("/quiz/{file_id}")
async def get_quiz(file_id: str, num_questions: int = 5, difficulty: str = "medium"):
    """Generate quiz questions from an uploaded file."""
    text = extract_text(file_id)
    if not text:
        raise HTTPException(404, "File not found or empty")

    questions = generate_quiz(text, num_questions, difficulty)
    return {"file_id": file_id, "questions": questions}


@app.post("/mindmap/{file_id}")
async def get_mindmap(file_id: str):
    """Generate a mind map from an uploaded file."""
    text = extract_text(file_id)
    if not text:
        raise HTTPException(404, "File not found or empty")

    mindmap = generate_mindmap(text)
    return {"file_id": file_id, "mindmap": mindmap}


@app.delete("/files/{file_id}")
async def remove_file(file_id: str):
    """Delete an uploaded file."""
    deleted = delete_file(file_id)
    if not deleted:
        raise HTTPException(404, "File not found")
    return {"deleted": True}
