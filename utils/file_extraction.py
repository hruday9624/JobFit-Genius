import fitz  # PyMuPDF
import docx
from io import BytesIO

import PyPDF2

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF using PyPDF2."""
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.strip()


def extract_text_from_docx(file):
    """Extract text from DOCX file (path or Streamlit UploadedFile)"""
    if hasattr(file, 'read'):  # Streamlit UploadedFile
        doc = docx.Document(BytesIO(file.read()))
    else:  # File path
        doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file):
    """Wrapper function to extract text based on file type"""
    if hasattr(file, 'name'):  # Streamlit UploadedFile
        filename = file.name.lower()
    else:  # File path
        filename = str(file).lower()
        
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file type")