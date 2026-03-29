from utils.api import call_llm

def map_to_target(predicates, target_text):
    prompt = f"""
    Map these predicates to target domain:
    {predicates}

    Target:
    {target_text}
    """
    response = call_llm(prompt)
    return response
