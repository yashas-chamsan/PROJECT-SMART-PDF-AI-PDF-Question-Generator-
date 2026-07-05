from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text

pdf_path = "data/uploads/sample.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

print("=" * 50)
print(f"Total Chunks: {len(chunks)}")
print("=" * 50)

print("\nFirst Chunk:\n")
print(chunks[0])

print("\n" + "=" * 50)

if len(chunks) > 1:
    print("\nSecond Chunk:\n")
    print(chunks[1])