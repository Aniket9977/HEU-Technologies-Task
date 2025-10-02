# HEU-Technologies-Task# Mini Agentic Pipeline

This project implements a **mini agentic pipeline** that:

- Retrieves relevant context from a small knowledge base (KB).
- Uses an LLM to reason and decide the next step.
- Executes an action via a tool (CSV, API, or web search).
- Produces a final answer along with a clear reasoning trace.

---

## Features

- **Retriever**: Uses embeddings and cosine similarity to find relevant KB documents.
- **Reasoner**: Uses OpenAI LLM (`gpt-4o-mini`) to decide whether to use the KB or call a tool.
- **Actor**: Simulates external tools; currently implemented with a CSV lookup.
- **Controller**: Orchestrates all components and returns the final answer.
- **Prompt Templates**: Modular system/user prompts, versioned for flexibility.
- **Environment-safe**: API keys loaded via `.env`.

---


---

## Requirements

- Python ≥ 3.9
- [OpenAI Python SDK](https://pypi.org/project/openai/) ≥ 2.0.1
- numpy
- python-dotenv (for loading environment variables)

Install dependencies:

```bash
pip install openai numpy python-dotenv
```

---


