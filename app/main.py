from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# データ構造の定義
class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    question: str
    answer: str

# ヘルスチェック
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 質問を受け取るエンドポイント
@app.post("/ask")
def ask(request: QuestionRequest) -> QuestionResponse:
    return QuestionResponse(
        question=request.question,
        answer=f"受け取りました：{request.question}"
    )