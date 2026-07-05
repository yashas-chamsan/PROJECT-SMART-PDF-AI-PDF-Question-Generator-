from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store

pdf_path = "data/uploads/sample.pdf"

# Step 1: Read PDF
text = extract_text_from_pdf(pdf_path)

# Step 2: Split into chunks
chunks = split_text(text)

# Step 3: Create embeddings
embeddings = create_embeddings(chunks)

# Step 4: Create FAISS index
index = create_vector_store(embeddings)

print("=" * 50)
print("FAISS Vector Store Created Successfully!")
print("=" * 50)

print(f"Total Chunks      : {len(chunks)}")
print(f"Total Embeddings  : {len(embeddings)}")
print(f"Vectors in FAISS  : {index.ntotal}")
print("=" * 50)