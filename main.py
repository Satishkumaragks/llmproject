import os
from xml.parsers.expat import model
from langchain_openai import ChatOpenAI
import openai
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


# for LM studio, we will use the local API endpoint and a different API token for testing.
API_TOKEN = os.getenv("API_TOKEN2")
BASE_URL = "http://127.0.0.1:1234/v1"


HEADERS = {
    "useLegacyCompletionsEndpoint": "false",
    "X-Tenant-ID": "default_tenant"
}


client = openai.OpenAI(
    api_key=API_TOKEN,
    base_url=BASE_URL,
    default_headers=HEADERS
)

models = client.models.list()
# // Print the list of models
for i, model in enumerate(models):
    print(f"{i + 1}. {model.id}")

# model=models[0]
llm = ChatOpenAI(
    model="nvidia/nemotron-3-nano-4b",
    api_key=API_TOKEN,
    base_url=BASE_URL,
    default_headers=HEADERS,
    # stream_usage=True,
    temperature=0.7,
    max_tokens=100
    # timeout=None,
    # reasoning_effort="low",
    # max_retries=2,
    # organization="...",
    # other params...
)



# llm = get_llm()
response = llm.invoke("Why do parrots talk?")
print(response.content)

