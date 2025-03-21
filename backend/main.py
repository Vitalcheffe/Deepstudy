from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Initialisation de Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint pour télécharger un fichier et l'analyser.
    """
    content = await file.read()
    # TODO: Ajouter la logique d'analyse avec DeepSeek AI
    return {"filename": file.filename, "content": content.decode("utf-8")}

@app.get("/summary/{file_id}")
async def get_summary(file_id: str):
    """
    Endpoint pour récupérer un résumé généré.
    """
    # TODO: Récupérer le résumé depuis Firebase
    return {"file_id": file_id, "summary": "Résumé généré par l'IA"}
