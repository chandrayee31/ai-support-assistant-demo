def analyze_with_llm(question: str, logs: dict) -> str:
    
    if "order" in question.lower():
        service_logs = logs.get("order-service", [])
        error_count = len(service_logs)

        return f"""
Root Cause Analysis:
The order service experienced {error_count} timeout-related errors today.

Primary Cause:
Payment gateway latency caused repeated request failures.

Suggested Fix:
- Scale the payment service
- Restart the affected Kafka consumer
- Add timeout retries
"""
    
    return "No relevant service issues found."
