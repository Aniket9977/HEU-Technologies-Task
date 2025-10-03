def run_eval(controller):
    test_queries = [
        "How much does Widget B cost?",
        "Tell me steps to maintain widgets.",
        "Price of Gadget X",
        "Price of Widget A",
        "Return policy for purchases"
    ]
    results = []
    for q in test_queries:
        res = controller.run_query(q)
        print("\nQuery:", q)
        print("Decision:", res["decision"])
        print("Answer:", res["final_answer"])
        results.append(res)
    return results
