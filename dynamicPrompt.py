import os
from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("API_TOKEN2")
BASE_URL = "http://127.0.0.1:1234/v1"


HEADERS = {
    "useLegacyCompletionsEndpoint": "false",
    "X-Tenant-ID": "default_tenant"
}


llm = ChatOpenAI(
    model="nvidia/nemotron-3-nano-4b",
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL,
    default_headers=HEADERS,
    temperature=0.7,
    max_tokens=1000
)

def get_input(prompt, default):
    value = input(f"{prompt} (default: {default}): ").strip()
    return value if value else default


# Dynamic input with defaults
role = get_input("Enter role", "teacher")
audience = get_input("Enter audience", "5-year-old")
topic = get_input("Enter topic", "What is Kubernetes?")

prompt = f"You are a {role}. Explain {topic} for {audience}"

response = llm.invoke([HumanMessage(content=prompt)])

print("\nExplanation:\n")
print(response.content)
