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


## Create a .env file in the project root
``` bash    
OPENAI_API_KEY=sk-your-key-here
```

## Verify environment variable
``` bash
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```


Should print your OpenAI API key.

## Run the pipeline
``` bash    

python main.py
```