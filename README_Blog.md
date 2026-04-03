# LangChain Advanced LCEL Blog Demo

This project demonstrates multiple LangChain LCEL patterns using a local OpenAI-compatible model endpoint.

## Main Script

- `blog.py`

The script loads a topic from user input and runs four different chain examples:

1. **Sequential chain**
  - Topic -> blog title -> blog content
2. **Multi-step SEO pipeline**
  - Topic -> keywords -> outline -> full article
3. **Parallel content generation**
  - Topic -> tweet + LinkedIn post + Instagram caption
4. **Enriched chain**
  - Keeps the original topic and combines it with generated keywords

## Technologies Used

- LangChain
- LangChain OpenAI integration
- LCEL (`PromptTemplate`, `RunnableParallel`, `RunnablePassthrough`)
- Local OpenAI-compatible endpoint
- Python dotenv

## Requirements

- Python 3.9+
- A running local or remote OpenAI-compatible API
- A model available at your configured endpoint

Current configuration in `blog.py`:

- Base URL: `http://127.0.0.1:1234/v1`
- Model: `nvidia/nemotron-3-nano-4b`

## Environment Variables

Create a `.env` file in the project root:

```env
API_TOKEN2=your_api_key_here
```

The script reads `API_TOKEN2` as `OPENAI_API_KEY`.

## Install Dependencies

```bash
pip install -r requirment.txt
```

If using the local virtual environment on Windows:

```bash
venv\Scripts\python.exe -m pip install -r requirment.txt
```

## Run the Demo

```bash
python blog.py
```

Or with the virtual environment interpreter:

```bash
venv\Scripts\python.exe blog.py
```

## Example Flow

When you run the script, it asks:

```text
Enter a topic:
```

If no topic is entered, it uses:

```text
Kubernetes
```

Then it prints output for all four chain examples.

## What `blog.py` Demonstrates

### 1. Sequential Chain

Uses two prompts in sequence:
- generate a title
- generate an article from that title

### 2. SEO Blog Pipeline

Builds a richer workflow by chaining:
- keyword generation
- outline creation
- detailed article generation

### 3. Parallel Chain

Uses `RunnableParallel` to generate multiple social media outputs at the same time:
- tweet
- LinkedIn post
- Instagram caption

### 4. Enriched Chain

Uses `RunnablePassthrough` to keep the original input while adding generated keywords before writing a blog introduction.

## Troubleshooting

If the script does not return content:

- Confirm your model server is running
- Confirm the base URL is correct
- Confirm `API_TOKEN2` is set in `.env`
- Confirm the selected model exists on the endpoint

If you get import errors, reinstall dependencies from `requirment.txt`.
