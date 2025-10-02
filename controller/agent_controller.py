import time

class AgentController:
    def __init__(self, store, reasoner, actor):
        self.store = store
        self.reasoner = reasoner
        self.actor = actor
        self.log = []

    def run_query(self, query):
        start = time.time()
        retrieved = self.store.search(query)
        decision = self.reasoner.decide_action(query, retrieved)

        if decision["action"] == "use_tool":
            tool_start = time.time()
            tool_response = self.actor.lookup(query)
            latency = (time.time() - tool_start) * 1000
            final_answer = f"Tool: {tool_response}" if tool_response else "No tool result."
        else:
            final_answer = decision.get("draft_answer","(no answer)")

        return {
            "query":query,
            "decision":decision,
            "retrieved":[r['doc']['meta'] for r in retrieved],
            "final_answer":final_answer,
            "latency_ms":(time.time()-start)*1000
        }
