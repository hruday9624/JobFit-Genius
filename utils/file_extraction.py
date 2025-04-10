import PyPDF2
import docx2txt
from typing import Optional, Union
from pathlib import Path
from streamlit.runtime.uploaded_file_manager import UploadedFile

def extract_text_from_pdf(file_path: Union[str, Path, UploadedFile]) -> str:
    """Extracts and returns text from a PDF file using PyPDF2."""
    text = ""
    try:
        if isinstance(file_path, UploadedFile):
            reader = PyPDF2.PdfReader(file_path)
        else:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.strip()

def extract_text_from_docx(file_path: Union[str, Path, UploadedFile]) -> str:
    """Extracts and returns text from a DOCX file."""
    try:
        if isinstance(file_path, UploadedFile):
            return docx2txt.process(file_path).strip()
        return docx2txt.process(str(file_path)).strip()
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

def extract_text(file_path: Union[str, Path, UploadedFile]) -> Optional[str]:
    """Detects file type and extracts text accordingly."""
    if isinstance(file_path, UploadedFile):
        file_name = file_path.name.lower()
    else:
        file_name = str(file_path).lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        print("Unsupported file format.")
        return None