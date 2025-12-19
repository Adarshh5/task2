import os
import json
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

app = FastAPI()

class Prompt(BaseModel):
    prompt: str
    debug: bool = False

@app.post("/generate")
async def generate_text(body: Prompt):
    headers = {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [{"text": body.prompt}]}
        ]
    }

    resp = requests.post(BASE_URL, headers=headers, json=payload)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()

    # extract main text
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        text = None

    result = {"generated_text": text}

    if body.debug:
        result["raw"] = data

    return result
