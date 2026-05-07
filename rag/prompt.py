def build_prompt(query, context):

    prompt = f"""
You are a macroeconomic analyst.

Use ONLY the context below to answer the question.

Context:
{context}

Rules:
- Be concise
- Avoid repetition
- Use evidence if available
- Do not generate code
- If unsure, say "Insufficient data available"

Question:
{query}

Answer:
"""

    return prompt