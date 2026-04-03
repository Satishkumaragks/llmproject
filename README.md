# First LLM App (LM Studio + LangChain)

This project runs a local chat model through the LM Studio OpenAI-compatible API using `LangChain` and `ChatOpenAI`.

## What `main.py` does

1. Loads environment variables from `.env`.
2. Reads `API_TOKEN2` as the API key.
3. Connects to LM Studio endpoint: `http://127.0.0.1:1234/v1`.
4. Lists available local models.
5. Creates a `ChatOpenAI` client with model:
   - `nvidia/nemotron-3-nano-4b`
6. Sends prompt: `Why do parrots talk?`
7. Prints model response.

## Requirements

Dependencies are listed in `requirment.txt`:

- langchain==0.3.28
- langchain-openai==0.3.35
- openai==2.29.0
- python-dotenv==1.2.1
- numpy==2.0.2
- certifi
- python-certifi-win32

## Setup

### 1) Install dependencies

```bash
pip install -r requirment.txt
```

### 2) Create `.env`

```env
API_TOKEN2=your_token_here
```

> Use any value accepted by your LM Studio/OpenAI-compatible local setup.

### 3) Start LM Studio local server

Make sure:
- A model is loaded in LM Studio.
- Local server is running at `http://127.0.0.1:1234`.

## Run

```bash
python main.py
```

## Expected output

- Printed list of available models.
- One generated response to: `Why do parrots talk?`

## Notes

- `BASE_URL` is hardcoded in `main.py`.
- The selected model in code must exist in your LM Studio model list.
- File name is currently `requirment.txt` (not `requirements.txt`).
