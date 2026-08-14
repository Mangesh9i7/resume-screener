import pymupdf
import docx

def parse_pdf(file_path):
    text = ""
    pdf_doc = pymupdf.open(file_path)
    for page in pdf_doc:
        text += page.get_text() + "\n"
    return text

def parse_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def parse_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_file(file_path):
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        return parse_docx(file_path)
    elif file_path.endswith(".txt"):
        return parse_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
