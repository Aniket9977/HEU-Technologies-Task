# Mini Agentic Pipeline

This project implements a **mini agentic pipeline** that retrieves context from a knowledge base, uses an LLM to reason about the next step, and optionally executes an external tool (like a CSV lookup) before returning the final answer.

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd mini_agent_pipeline
```

--- 

## Install dependencies
```bash
pip install openai numpy python-dotenv
```

--- 
## Create a .env file in the project root
``` bash    
OPENAI_API_KEY=sk-your-key-here
```
--- 

## Verify environment variable
``` bash
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```
--- 

Should print your OpenAI API key.

## Run the pipeline
``` bash    

python main.py
```

--- 



# Design 

## Modular Architecture

store/ → Retrieval layer over a small KB (CSV-based for simplicity).

reasoner/ → Uses OpenAI’s GPT models to decide whether to use KB or external tool.

actor/ → A simple lookup tool (CSV search for products, policies, etc.).

controller/ → Orchestrates retrieval, reasoning, action, and evaluation.

## LLM as Decision Maker

Prompts are structured so the LLM must respond with strict JSON ({"action":"use_tool"} or {"action":"use_kb"}).

If JSON parsing fails, a fallback is used (parse_fail).

## Logging & Evaluation

Latencies and decisions are logged.

eval/ module runs a set of test queries and measures pipeline performance.

## Simplicity Over Complexity

Instead of vector embeddings, a lightweight keyword-based search (pandas filtering) is used.

Tools are mocked as CSV lookups, but design allows plugging in real APIs.



# Known Limitations

## Fragile JSON Parsing
The LLM may sometimes return extra text/markdown around JSON, causing parse_fail. A stricter prompt or regex cleaning may be needed.

## Shallow Retrieval
Current retrieval uses simple string matching on CSV. For better recall/precision, embeddings or vector search should replace it.

## Draft Answer Quality
If the LLM outputs "use_kb" but no good draft answer, the system falls back to raw snippets, which may be irrelevant.

## Single Tool Actor
Only a CSV lookup tool is implemented. Adding multiple tools will require tool selection logic.


## Environment Key Handling
The pipeline requires OPENAI_API_KEY in .env. If missing, initialization will fail.



# Video Link
```bash
https://www.youtube.com/watch?v=ULuiJOHk3oc

```