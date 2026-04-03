# LongChain Prompt Demo

This project runs a simple interactive prompt using LangChain + OpenAI-compatible API.

## File Overview

- `dynamicPrompt.py`: Main script that:
  - Loads environment variables from `.env`
  - Creates a `ChatOpenAI` client
  - Asks for `role`, `audience`, and `topic`
  - Sends a prompt to the model and prints the response
- `main.py`: Additional test script
- `requirment.txt`: Python dependencies

## Requirements

- Python 3.9+
- A running OpenAI-compatible endpoint (current config uses LM Studio):
  - `http://127.0.0.1:1234/v1`
- API token set in `.env`

## Environment Variables

Create a `.env` file in the project root:

```env
API_TOKEN2=your_api_key_here
```

`dynamicPrompt.py` reads `API_TOKEN2`.

## Install Dependencies

```bash
pip install -r requirment.txt
```

If you are using the project virtual environment on Windows:

```bash
venv\Scripts\python.exe -m pip install -r requirment.txt
```

## Run

```bash
python dynamicPrompt.py
```

Or with venv Python:

```bash
venv\Scripts\python.exe dynamicPrompt.py
```

You will be prompted for:
- role (default: `teacher`)
- audience (default: `5-year-old`)
- topic (default: `What is Kubernetes?`)

Then the script prints the model explanation.

## Notes

- Model currently configured: `nvidia/nemotron-3-nano-4b`
- If output is blank, verify:
  - Your local model is loaded and running
  - `BASE_URL` is reachable
  - `API_TOKEN2` is present in `.env`
