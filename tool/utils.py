from pdfminer.high_level import extract_text as pdf_extract
from docx import Document

def extract_text_from_file(path: str) -> str:
    """Extract text from PDF, DOCX, or TXT."""
    path_lower = path.lower()

    try:
        if path_lower.endswith(".pdf"):
            return pdf_extract(path)

        if path_lower.endswith(".docx"):
            doc = Document(path)
            return "\n".join([p.text for p in doc.paragraphs])

        if path_lower.endswith(".txt"):
            with open(path, "r", encoding="utf8") as f:
                return f.read()

        return ""
    except Exception as e:
        return f"[Extraction Error: {e}]"

