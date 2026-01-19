from fastapi import FastAPI
from pydantic import BaseModel
from news_summarizer import summarize_news
from dotenv import load_dotenv
from pathlib import Path
import os

# Create FastAPI app FIRST
app = FastAPI()

# Load .env - FIXED WINDOWS ESCAPE ISSUE
env_path = Path("C:/Users/sashi/OneDrive/Documents/Langchain/RAG/.env")
load_dotenv(env_path)

# Confirm keys loaded
print("Loaded NEWSAPI_KEY =", os.getenv("NEWSAPI_KEY"))
print("Loaded TAVILY_API_KEY =", os.getenv("TAVILY_API_KEY"))
print("Loaded OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))


class Query(BaseModel):
    question: str


@app.post("/summarize")
def summarize_api(payload: Query):
    result = summarize_news(payload.question)
    return result
