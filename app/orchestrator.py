from app.mock_data_loader import load_fake_logs
from app.llm_client import analyze_with_llm


def process_question(question: str):
    print("✅ Question received:", question)

    print("✅ Fetching system logs...")
    logs = load_fake_logs()

    print("✅ Sending logs + question to LLM...")
    answer = analyze_with_llm(question, logs)

    print("✅ Response ready.")
    return answer
