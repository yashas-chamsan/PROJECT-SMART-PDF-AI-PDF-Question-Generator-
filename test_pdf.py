from src.pdf_loader import extract_text_from_pdf
pdf_path = "data/uploads/sample.pdf"
text = extract_text_from_pdf(pdf_path)

print("=" * 500)
print("PDF LOADED SUCCESSFULLY!")
print("=" *50)

print(text[:1000])