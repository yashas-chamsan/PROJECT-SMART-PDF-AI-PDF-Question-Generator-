from src.llm import generate_answer


def generate_questions(context):
    """
    Generates different types of questions from the PDF context.
    """

    prompt = """
Generate the following using ONLY the given context:

1. Five Multiple Choice Questions (MCQs)
   - Include four options
   - Mention the correct answer

2. Five Short Answer Questions

3. Five Long Answer Questions

If the context is insufficient, mention that clearly.

Context:
""" + context

    questions = generate_answer(prompt, context)

    return questions