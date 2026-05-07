from rag.retriever import retrieve_context
from rag.prompt import build_prompt
import ollama


def generate_answer(prompt):
    response = ollama.chat(
        model="phi",
        messages=[{"role": "user", "content": prompt}],
        options={
        "num_predict": 150
    }
    )
    return response["message"]["content"]


def chatbot(query, kb, index):
    context = retrieve_context(query, kb, index)
    prompt = build_prompt(query, context)
    answer = generate_answer(prompt)
    return answer