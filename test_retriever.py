from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_chunks

pdf_path = "data/uploads/sample.pdf"

# Step 1: Read PDF
text = extract_text_from_pdf(pdf_path)

# Step 2: Split into chunks
chunks = split_text(text)

# Step 3: Create embeddings
embeddings = create_embeddings(chunks)

# Step 4: Create FAISS index
index = create_vector_store(embeddings)

# Step 5: Ask a question
question = "What is Artificial Intelligence?"

results = retrieve_chunks(
    index=index,
    model=model,
    chunks=chunks,
    question=question,
    k=3
)

print("=" * 60)
print("QUESTION:")
print(question)
print("=" * 60)

for i, chunk in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 60)
    print(chunk[:500])