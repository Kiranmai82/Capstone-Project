import PyPDF2


def extract_pdf_text(uploaded_file):
    """Extract text from a PDF uploaded file-like object."""
    if hasattr(uploaded_file, "seek"):
        uploaded_file.seek(0)

    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        page_texts = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                page_texts.append(text)
        return "\n".join(page_texts)
    except Exception:
        return ""
