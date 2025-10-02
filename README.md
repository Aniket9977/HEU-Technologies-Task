# HEU-Technologies-Task# Mini Agentic Pipeline

This project implements a **mini agentic pipeline** that:

- Retrieves relevant context from a small knowledge base (KB).
- Uses an LLM to reason and decide the next step.
- Executes an action via a tool (CSV, API, or web search).
- Produces a final answer along with a clear reasoning trace.




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


