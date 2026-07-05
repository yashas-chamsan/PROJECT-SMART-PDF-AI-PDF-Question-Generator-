from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings

pdf_path = "data/uploads/sample.pdf"

# Read PDF
text = extract_text_from_pdf(pdf_path)

# Split into chunks
chunks = split_text(text)

# Create embeddings
embeddings = create_embeddings(chunks)

print("=" * 50)
print(f"Total Chunks: {len(chunks)}")
print(f"Total Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")
print("=" * 50)

print("\nFirst Chunk:\n")
print(chunks[0][:200])

print("\nFirst Embedding (first 10 numbers):\n")
print(embeddings[0][:10])