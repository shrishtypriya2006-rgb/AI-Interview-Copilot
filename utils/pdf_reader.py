from pypdf import PdfReader

def extract_text(pdf_file):
    """
    Extract text from uploaded PDF.
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text