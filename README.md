
# Deep Study AI

![Python](https://img.shields.io/badge/python-3.10-blue)
![JavaScript](https://img.shields.io/badge/javascript-ES6-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What the Project Does

Deep Study AI is an educational application designed to help students transform raw course material into structured learning resources such as summaries, revision notes, quizzes, and mind maps.

The project is built as a full-stack application, with a clear separation between backend logic (content processing and generation) and frontend interfaces (user interaction and visualization).

---

## Why the Project Is Useful

Studying often means dealing with long, unstructured documents. Deep Study AI focuses on turning that chaos into clarity.

Main benefits include:

- Automatic summarization of course content  
- Clear and organized revision sheets  
- Quiz generation to test understanding  
- Mind maps to visualize relationships between concepts  
- A complete backend–frontend architecture suitable for real-world projects  

This project is useful for students, educators, and developers interested in educational tools, productivity, and structured learning workflows.

---

## How Users Can Get Started

### Prerequisites

- Python 3.10 or higher  
- Node.js and npm  
- A Firebase account (authentication and data storage)

---

## Installation

### Clone the repository
```bash

git clone https://github.com/Vitalcheffe/Deepstudy.git

cd Deepstudy

### Backend setup

pip install -r backend/requirements.txt

### Frontend setup

npm install

### Firebase configuration

Configure Firebase by filling in the `firebase-config.json` file with your own credentials.

---

## Launching the Project

### Start the backend server

uvicorn backend.main:app --reload

### Start the frontend application

npm start

---

## Usage

1. Start both the backend and frontend  
2. Submit a course or study text through the interface  
3. Receive generated summaries, revision notes, quizzes, and mind maps  
4. Use the generated content to study, revise, or teach more effectively  

---

## Technologies Used

- Backend: Python, FastAPI  
- Frontend: JavaScript, React  
- Authentication & Database: Firebase  

---

## Project Maintenance

Maintained by **Vitalcheffe**.

Contributions are welcome through pull requests or GitHub issues.  
Feel free to suggest improvements, report bugs, or extend features.

---

## License

This project is licensed under the MIT License.  
See the LICENSE file for more details.
