from utils.lexicon import EXCLUSION_TERMS

def verify(predicates):
    if len(predicates) < 3:
        return False, "Too few predicates"

    has_higher = any(p.get("type") == "higher" for p in predicates)
    if not has_higher:
        return False, "No higher-order relation"

    for p in predicates:
        text = p["name"].lower()
        if any(word in text for word in EXCLUSION_TERMS):
            return False, "Contains attribute-based term"

    return True, "Pass"
