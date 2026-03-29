import requests
import os

API_KEY = os.getenv("ANTHROPIC_API_KEY")

def call_llm(prompt):
    # Replace with real Anthropic API if needed
    return mock_response(prompt)


def mock_response(prompt):
    # simple placeholder so your code runs
    return {
        "predicates": [
            {"name": "CAUSES", "args": ["A", "B"], "type": "higher"}
        ]
    }
