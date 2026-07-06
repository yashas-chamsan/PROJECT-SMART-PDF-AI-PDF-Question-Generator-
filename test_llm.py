from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_chunks
from src.llm import generate_answer

pdf_path = "data/uploads/sample.pdf"

# Step 1: Read PDF
text = extract_text_from_pdf(pdf_path)

# Step 2: Split into chunks
chunks = split_text(text)

# Step 3: Create embeddings
embeddings = create_embeddings(chunks)

# Step 4: Create FAISS index
index = create_vector_store(embeddings)

# Step 5: User question
question = "What is Artificial Intelligence?"

# Step 6: Retrieve relevant chunks
retrieved_chunks = retrieve_chunks(
    index=index,
    model=model,
    chunks=chunks,
    question=question,
    k=3
)

# Step 7: Combine retrieved chunks into one context
context = "\n\n".join(retrieved_chunks)

# Step 8: Generate answer
answer = generate_answer(question, context)

print("=" * 60)
print("QUESTION:")
print(question)
print("=" * 60)

print("\nANSWER:\n")
print(answer)