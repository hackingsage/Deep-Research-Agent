from ..models.groq_client import generate_response


def self_reflect_node(state):

    critique_prompt = f"""
You are a senior research engineer reviewing an AI-generated answer.

User Question:
{state['query']}

Draft Answer:
{state['answer']}

Your task:
1. Identify missing technical depth
2. Detect vague explanations
3. Improve clarity and correctness
4. Add practical engineering insight if missing

Return ONLY the improved final answer.
"""

    improved_answer = generate_response(critique_prompt)

    state["answer"] = improved_answer
    return state