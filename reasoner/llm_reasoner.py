from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

LLM_MODEL = "gpt-4o-mini"
PROMPT_TEMPLATES = {
    "v1": {
        "system": "You are a concise decision-making assistant...",
        "user": (
            "Query: {query}\n\nRetrieved snippets:\n{snippets}\n\n"
            "Decide: use_tool or use_kb, return JSON."
        )
    }
}

class LLMReasoner:
    def __init__(self, model=LLM_MODEL, templates=PROMPT_TEMPLATES):
        self.model = model
        self.templates = templates

    def llm_call(self, system_msg, user_msg):
        resp = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.0
        )
        # Access as object attributes, not dict
        return resp.choices[0].message.content

    def decide_action(self, query, retrieved, version="v1"):
        snippets = "\n".join(f"- {r['doc']['text'][:100]}" for r in retrieved)
        templ = self.templates[version]
        raw = self.llm_call(templ["system"], templ["user"].format(query=query, snippets=snippets))
        try:
            return json.loads(raw)
        except:
            return {"action":"use_kb","reason":"parse_fail","draft_answer":raw}
