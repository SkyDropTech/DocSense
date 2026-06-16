import os
from pypdf import PdfReader
import docx

def parse_document(file_path: str, filename: str) -> str:
    text = ""
    ext = os.path.splitext(filename)[1].lower()
    
    try:
        if ext == ".pdf":
            reader = PdfReader(file_path)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + " "
        elif ext == ".docx":
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")
        
    return text