from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

LLM_MODEL = "gpt-4o-mini"
PROMPT_TEMPLATES = {
    "v1": {
        "system": (
            "You are an intelligent assistant that decides the best course of action to answer a user's query. "
            "You have access to a knowledge base (KB) and an external tool for price lookups.\n\n"
            "1.  If the query is about product pricing, decide to `use_tool`.\n"
            "2.  If the retrieved KB snippets can answer the query, decide to `use_kb` and provide a concise answer based *only* on the snippets.\n"
            "3.  Respond ONLY with a valid JSON object with the fields `action` (string: 'use_tool' or 'use_kb'), `reason` (string: your reasoning), and `draft_answer` (string: your generated answer if action is 'use_kb', otherwise null)."
        ),
        "user": (
            "Query: {query}\n\n"
            "Retrieved KB snippets:\n{snippets}"
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
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        # Access as object attributes, not dict
        return resp.choices[0].message.content

    def decide_action(self, query, retrieved, version="v1"):
        snippets = "\n".join(f"- {r['doc']['text'][:200]}" for r in retrieved)
        templ = self.templates[version]
        raw = self.llm_call(
            templ["system"],
            templ["user"].format(query=query, snippets=snippets)
        )
        try:
            parsed = json.loads(raw)
            return parsed
        except (json.JSONDecodeError, TypeError):
            return {"action": "use_kb", "reason": "parse_fail", "draft_answer": raw}
