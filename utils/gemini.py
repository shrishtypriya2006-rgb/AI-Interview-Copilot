import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_questions(resume_text, job_role, experience):

    prompt = f"""
You are an expert interviewer.

Resume:
{resume_text}

Job Role:
{job_role}

Experience:
{experience}

Generate exactly 5 interview questions.

Return only the questions.
"""

    response = model.generate_content(prompt)

    return response.text