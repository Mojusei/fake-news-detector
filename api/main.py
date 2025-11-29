# api/main.py
"""Точка входа FastAPI-сервиса."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.schemas import NewsResponse, NewsInput
from src.predict import predict_news

app = FastAPI(
    title="Fake News Detector",
    description="Распознаватель фейковых новостей",
    version="0.1.0"
)


@app.post('/predict', response_model=NewsResponse)
async def predict(input_data: NewsInput):
    try:
        answer = predict_news(input_data.text)
        return NewsResponse(answer=answer)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "message": "Prediction failed"}
        )


@app.get("/health")
async def health_check():
    return {"status": "OK"}
