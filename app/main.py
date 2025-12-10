from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import process_question

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_system(request: QueryRequest):
    answer = process_question(request.question)
    return {"answer": answer}
