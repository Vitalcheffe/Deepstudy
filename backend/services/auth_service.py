"""
Deep Study AI — Auth Service
Firebase authentication integration.
"""

import os
import logging
from typing import Optional

log = logging.getLogger(__name__)

try:
    import firebase_admin
    from firebase_admin import auth as firebase_auth
    _initialized = firebase_admin._apps
except ImportError:
    _initialized = False
    log.warning("firebase-admin not installed")


def verify_token(id_token: str) -> Optional[dict]:
    """Verify a Firebase ID token and return user info."""
    if not _initialized:
        log.error("Firebase not initialized")
        return None

    try:
        decoded = firebase_auth.verify_id_token(id_token)
        return {
            "uid": decoded.get("uid"),
            "email": decoded.get("email"),
            "name": decoded.get("name", ""),
            "email_verified": decoded.get("email_verified", False),
        }
    except Exception as e:
        log.error("Token verification failed: %s", e)
        return None


def get_user(uid: str) -> Optional[dict]:
    """Get user info by UID."""
    if not _initialized:
        return None

    try:
        user = firebase_auth.get_user(uid)
        return {
            "uid": user.uid,
            "email": user.email,
            "display_name": user.display_name,
            "disabled": user.disabled,
        }
    except Exception as e:
        log.error("Get user failed: %s", e)
        return None
