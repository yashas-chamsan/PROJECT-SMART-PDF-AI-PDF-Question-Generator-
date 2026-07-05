import fitz #PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF and returns all the text as a single string.
    """

    document = fitz.open(pdf_path)
    text=""
    for page in document:
        text += page.get_text()
        
    document.close()
    
    return text