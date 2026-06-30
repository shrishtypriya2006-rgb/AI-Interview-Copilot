from utils.gemini import model

def evaluate_answer(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer using the following format.

Score: /10

Strengths:
- Point 1
- Point 2

Weaknesses:
- Point 1
- Point 2

Ideal Answer:
Write a concise ideal answer.
"""

    response = model.generate_content(prompt)

    return response.text