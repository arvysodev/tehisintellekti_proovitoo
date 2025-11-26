from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .qa_service import answer_question


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


app = FastAPI(title="Tehisintellekt.ee Q&A")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = BASE_DIR / "frontend"
INDEX_FILE = FRONTEND_DIR / "index.html"

@app.get("/")
def index():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AnswerResponse)
def ask(req: QuestionRequest):
    answer = answer_question(req.question)
    return AnswerResponse(answer=answer)
