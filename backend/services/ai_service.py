"""
Deep Study AI — AI Service
Handles content generation: summaries, quizzes, mind maps.
"""

import os
import logging
from typing import Optional

log = logging.getLogger(__name__)

try:
    import openai
    _client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
    _available = True
except ImportError:
    _available = False
    log.warning("openai not installed, AI features disabled")


def generate_summary(text: str, max_tokens: int = 1000) -> str:
    """Generate a concise summary from raw course material."""
    if not _available or not text.strip():
        return "AI service unavailable. Please install openai and set OPENAI_API_KEY."

    try:
        response = _client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a study assistant. Summarize the following course material into clear, concise revision notes. Use bullet points and headers."},
                {"role": "user", "content": text[:4000]},
            ],
            max_tokens=max_tokens,
            temperature=0.3,
        )
        return response.choices[0].message.content or ""
    except Exception as e:
        log.error("Summary generation failed: %s", e)
        return f"Error generating summary: {e}"


def generate_quiz(text: str, num_questions: int = 5, difficulty: str = "medium") -> list[dict]:
    """Generate quiz questions from course material."""
    if not _available or not text.strip():
        return []

    try:
        response = _client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Generate {num_questions} multiple-choice quiz questions at {difficulty} difficulty from the following material. Return JSON array with: question, options (4 choices), answer (index 0-3), explanation."},
                {"role": "user", "content": text[:4000]},
            ],
            max_tokens=2000,
            temperature=0.5,
        )
        import json
        content = response.choices[0].message.content or "[]"
        # Extract JSON from markdown code blocks if present
        if "```" in content:
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        return json.loads(content.strip())
    except Exception as e:
        log.error("Quiz generation failed: %s", e)
        return []


def generate_mindmap(text: str) -> dict:
    """Generate a mind map structure from course material."""
    if not _available or not text.strip():
        return {"topic": "Error", "branches": []}

    try:
        response = _client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Create a mind map from this material. Return JSON with: topic (string), branches (array of {label, children: [string]})"},
                {"role": "user", "content": text[:4000]},
            ],
            max_tokens=1500,
            temperature=0.4,
        )
        import json
        content = response.choices[0].message.content or "{}"
        if "```" in content:
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        return json.loads(content.strip())
    except Exception as e:
        log.error("Mind map generation failed: %s", e)
        return {"topic": "Error", "branches": []}


def is_available() -> bool:
    """Check if AI service is configured."""
    return _available and bool(os.getenv("OPENAI_API_KEY"))
