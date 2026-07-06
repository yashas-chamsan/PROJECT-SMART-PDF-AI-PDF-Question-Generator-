from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_chunks
from src.question_generator import generate_questions

pdf_path = "data/uploads/sample.pdf"

# Step 1: Read PDF
text = extract_text_from_pdf(pdf_path)

# Step 2: Split text
chunks = split_text(text)

# Step 3: Create embeddings
embeddings = create_embeddings(chunks)

# Step 4: Create FAISS index
index = create_vector_store(embeddings)

# Step 5: Retrieve relevant chunks
context_chunks = retrieve_chunks(
    index=index,
    model=model,
    chunks=chunks,
    question="Generate important exam questions from this PDF.",
    k=8
)

# Step 6: Combine chunks
context = "\n\n".join(context_chunks)

# Step 7: Generate questions
questions = generate_questions(context)

print("=" * 70)
print("GENERATED QUESTIONS")
print("=" * 70)
print(questions)