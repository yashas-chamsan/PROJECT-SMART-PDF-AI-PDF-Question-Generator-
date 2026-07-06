import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API key from .env
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, context):
    """
    Generates an answer using the retrieved PDF context.
    """

    prompt = f"""
You are an AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:
"I couldn't find that information in the PDF."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text