import re
from typing import Union, IO
import pdfplumber
import PyPDF2
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Basic stopwords (optional, since spaCy has its own)
_BASIC_STOPWORDS = {
    "the","and","is","in","to","of","a","for","on","with","as","at","by","an","be",
    "this","that","are","from","or","it","your","you","we","our","their","they",
    "will","can","have","has","had","but","not","if","about","into","over","under",
    "per","via","than","then","so","such","these","those","within","without"
}

def extract_text_from_pdf(pdf_source: Union[str, IO[bytes]]) -> str:
    """Extract text from a PDF using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_source) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception:
        return ""
    return text

def preprocess_text(text: str):
    """Tokenize, lemmatize, and remove stopwords using spaCy."""
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def extract_links_from_pdf(pdf_source: Union[str, IO[bytes]]):
    """Extract hyperlink URLs from PDF annotations if present."""
    links = []
    try:
        reader = pdf_source if hasattr(pdf_source, "read") else open(pdf_source, "rb")
        reader = PyPDF2.PdfReader(reader)
        for page in reader.pages:
            annots = page.get("/Annots")
            if not annots:
                continue
            for annot_ref in annots:
                try:
                    annot = annot_ref.get_object()
                    action = annot.get("/A") if annot else None
                    uri = action.get("/URI") if action else None
                    if uri and isinstance(uri, str):
                        links.append(uri)
                except Exception:
                    continue
    except Exception:
        return []
    return links

def extract_contacts(text: str, pdf_source: Union[str, IO[bytes], None] = None):
    """Extract linkedin, github, email, and phone from text and PDF links."""
    url_pattern = r"(https?://[^\s)]+|www\.[^\s)]+)"
    urls_from_text = re.findall(url_pattern, text, flags=re.IGNORECASE)
    urls_from_pdf = extract_links_from_pdf(pdf_source) if pdf_source else []
    all_urls = {u.strip() for u in urls_from_text + urls_from_pdf}

    linkedin = next((u for u in all_urls if "linkedin.com" in u.lower()), "")
    github = next((u for u in all_urls if "github.com" in u.lower()), "")

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)
    email = emails[0] if emails else ""

    phone_pattern = r"(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?|\d{4}[\s.-]?)\d{3,4}[\s.-]?\d{4}"
    phones = re.findall(phone_pattern, text)
    phone = phones[0] if phones else ""

    return {
        "linkedin": linkedin,
        "github": github,
        "email": email,
        "phone": phone,
    }

def get_keywords(text: str):
    tokens = preprocess_text(text)
    return set(tokens)

def match_score(resume_keywords: set, job_keywords: set):
    if not job_keywords:
        return 0.0, set()
    matched = resume_keywords.intersection(job_keywords)
    score = (len(matched) / len(job_keywords)) * 100.0
    return score, matched
