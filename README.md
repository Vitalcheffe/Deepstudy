# Deep Study AI

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/javascript-ES6-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## What the Project Does

Deep Study AI is an educational application that helps students transform raw course materials into structured learning tools such as summaries, revision notes, quizzes, and mind maps.

The project follows a full-stack architecture with a clear separation between backend logic and frontend interface.

---

## Why the Project Is Useful

Deep Study AI aims to improve learning efficiency by automating content structuring.

Main benefits:
- Automatic generation of concise summaries from raw text
- Structured revision sheets for faster review
- Quiz generation to test understanding
- Mind map creation to visualize relationships between concepts
- Practical example of a modern full-stack application

This project is relevant for students, educators, and developers interested in educational technology.

---

## How Users Can Get Started

### Prerequisites

- Python 3.10 or higher
- Node.js and npm
- A Firebase project for authentication and data storage

### Installation

Clone the repository:

```
git clone https://github.com/Vitalcheffe/Deepstudy.git
cd Deepstudy
```

Install backend dependencies:

```
pip install -r backend/requirements.txt
```

Install frontend dependencies:

```
npm install
```

Configure Firebase using the `firebase-config.json` file.

---

## Running the Project

Start the backend server:

```
uvicorn backend.main:app --reload
```

Start the frontend application:

```
npm start
```

---

## Usage

- Launch both backend and frontend
- Submit course or study material
- Receive generated summaries, revision notes, quizzes, and mind maps
- Use the generated content for studying or teaching

---

## Technologies Used

- Backend: Python, FastAPI
- Frontend: JavaScript, React
- Authentication and Database: Firebase

---

## Maintenance and Contributions

Maintained by **Vitalcheffe**.

Contributions are welcome through pull requests and issues.  
Please keep changes focused and well-documented.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for more information.
