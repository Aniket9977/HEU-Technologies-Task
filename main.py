from retriever.vector_store import SimpleVectorStore
from reasoner.llm_reasoner import LLMReasoner
from actor.csv_actor import CSVActor
from controller.agent_controller import AgentController
from eval.evaluation import run_eval
from pathlib import Path

def ensure_demo_docs():
    Path("data/docs").mkdir(parents=True, exist_ok=True)
    demo_docs = [
        ("doc1.txt","Widget A is a small, inexpensive gadget..."),
        ("doc2.txt","Widget B is an upgraded widget..."),
        ("doc3.txt","Return policy: within 30 days...")
    ]
    for fname, text in demo_docs:
        p = Path("data/docs")/fname
        if not p.exists():
            p.write_text(text)

def load_docs():
    docs = []
    for i,p in enumerate(Path("data/docs").glob("*.txt")):
        docs.append({"id":str(i),"text":p.read_text(),"meta":{"source":p.name}})
    return docs

if __name__=="__main__":
    ensure_demo_docs()
    docs = load_docs()

    store = SimpleVectorStore()
    store.add_docs(docs)
    store.build_index()

    reasoner = LLMReasoner()
    actor = CSVActor()
    controller = AgentController(store, reasoner, actor)

    run_eval(controller)
