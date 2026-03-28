"""
Firebase utility helpers.
"""

import os
import logging

log = logging.getLogger(__name__)

try:
    import firebase_admin
    from firebase_admin import firestore, storage

    def get_db():
        """Get Firestore client."""
        return firestore.client()

    def get_bucket():
        """Get Cloud Storage bucket."""
        return storage.bucket()

except ImportError:
    log.warning("firebase-admin not installed")

    def get_db():
        raise RuntimeError("firebase-admin not installed")

    def get_bucket():
        raise RuntimeError("firebase-admin not installed")
