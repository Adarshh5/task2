# Minimal AI Service — Gemini API Integration

A lightweight FastAPI-based AI service that forwards user prompts to Google’s **Gemini 2.0 Flash** model and returns the generated response.  
Built as part of Task B — API Integration, with additional sections for DSA and RAG/FAISS tasks.

---

## 🚀 Features

- Simple REST API using FastAPI
- Forwards prompts to Gemini 2.0 Flash
- Returns clean generated text
- Optional debug mode to view raw API response
- Minimal, easy-to-read implementation

---

## 🧰 Tech Stack

- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- python-dotenv

---

## 📁 Project Structure

.
├── main.py
├── .env
├── requirements.txt
└── README.md




---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Adarshh5/task2.git
cd task1



2️⃣ Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add environment variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here


Get your API key from: https://ai.google.dev/

▶️ Running the Server
uvicorn main:app --reload --port 8000


Server will start at:

http://localhost:8000