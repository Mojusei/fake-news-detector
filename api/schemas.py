# api/schemas.py
"""Pydantic-модели для валидации запросов и ответов."""

from pydantic import BaseModel, Field
from config.globals import MIN_LENGTH_INPUT_NEWS, MAX_LENGTH_INPUT_NEWS


class NewsInput(BaseModel):
    text: str = Field(
        ..., min_length=MIN_LENGTH_INPUT_NEWS, max_length=MAX_LENGTH_INPUT_NEWS
        )


class NewsResponse(BaseModel):
    answer: str
    message: str = "OK"
