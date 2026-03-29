from utils.api import call_llm

def extract_relations(source_text):
    prompt = f"Extract relational predicates:\n{source_text}"
    response = call_llm(prompt)

    return response  # expected JSON
