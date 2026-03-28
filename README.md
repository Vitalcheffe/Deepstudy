<h1 align="center">Deep Study AI</h1>
<p align="center">Transform raw course materials into structured learning tools.<br/>Summaries, quizzes, mind maps.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/React-Native-blue?logo=react" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

## What

Upload your course materials. Get back structured summaries, revision sheets, quizzes, and mind maps. Powered by AI.

## Architecture

```
Frontend (React Native)  →  Backend (FastAPI)  →  AI Service (DeepSeek/OpenAI)
                                              →  Firebase (auth + storage)
                                              →  Stripe (payments)
```

## Stack

- **Backend:** Python, FastAPI, Firebase Admin, Stripe
- **Frontend:** React Native, JavaScript
- **AI:** DeepSeek / OpenAI API
- **Auth & DB:** Firebase
- **Payments:** Stripe

## Run it

Backend:
```bash
pip install -r backend/requirements.txt
cp .env.example .env  # add your keys
uvicorn backend.main:app --reload
```

Frontend:
```bash
cd frontend && npm install && npm start
```

## Structure

```
backend/
├── main.py              # FastAPI endpoints
├── services/
│   ├── ai_service.py    # AI generation
│   ├── auth_service.py  # Authentication
│   └── file_service.py  # File handling
├── utils/
│   ├── firebase.py      # Firebase integration
│   └── stripe.py        # Payment handling
└── tests/

frontend/
├── screens/             # App screens
├── components/          # UI components
├── services/            # API, auth, storage
└── firebase-config.js
```

## Status

⚠️ Work in progress. Backend endpoints are scaffolded, frontend screens are built. AI service integration is in development.

---

<p align="center">
  <sub>Amine Harch · 16 · Casablanca · <a href="https://vitalcheffe.github.io">vitalcheffe.github.io</a></sub>
</p>
