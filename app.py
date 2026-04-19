import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from src.engine.analyzer import fetch_transaction_data, calculate_risk

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/analyze")
def analyze(signature: str):
    data = fetch_transaction_data(signature)

    if not data:
        return {"status": "error"}

    level, score = calculate_risk(data)

    return {
        "status": "ok",
        "level": level,
        "score": score
    }