import os
import re
import io
from PyPDF2 import PdfReader
from docx import Document
import docx2txt
import textract

from .constants import (
    EMAIL_REGEX,
    PHONE_REGEX,
    HARD_SKILLS,
    LINKEDIN_REGEX,
    GITHUB_REGEX,
    PORTFOLIO_REGEX
)
#degree
def extract_degree_patterns(text):
    degree_keywords = [
        "bachelor", "b.tech", "b. tech","btech", "b.e", "be", "b.sc", "msc", "m.tech", "mtech", "master", "phd", "mba", "bca", "mca"
    ]
    pattern = re.compile(r'\b(?:' + '|'.join(degree_keywords) + r')\b', re.IGNORECASE)
    return list(set(match.group().upper() for match in re.finditer(pattern, text)))

def extract_name_heuristic(text):
    lines = text.split('\n')[:10]  # Check top 10 lines
    for line in lines:
        line = line.strip()
        if line and not any(x in line.lower() for x in ['resume', 'curriculum', 'vitae']):
            words = line.split()
            if 1 < len(words) <= 4:
                words_clean = [w for w in words if w.isalpha() and w.upper() == w and len(w) > 1]
                if len(words_clean) >= 2:
                    return ' '.join(words_clean[:2])
    return None


# ========= 1. Extract Raw Text from Resume ==========

def extract_text(file, ext):
    ext = ext.lower()
    if isinstance(file, io.BytesIO):
        file.seek(0)
    if ext == ".pdf":
        return extract_pdf_text(file)
    elif ext == ".docx":
        return extract_docx_text(file)
    else:
        return extract_other_text(file)

def extract_pdf_text(file):
    try:
        pdf = PdfReader(file)
        return "\n".join([page.extract_text() or "" for page in pdf.pages])
    except Exception:
        return ""

def extract_docx_text(file):
    try:
        return docx2txt.process(file)
    except Exception:
        try:
            doc = Document(file)
            return "\n".join([p.text for p in doc.paragraphs])
        except:
            return ""

def extract_other_text(file):
    try:
        return textract.process(file).decode("utf-8")
    except:
        return ""

# ========= 2. Entity Extraction ==========

def extract_entities_with_custom_model(doc):
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)
    return entities

# ========= 3. Email, Phone, Name ==========

def extract_email(text):
    match = re.search(EMAIL_REGEX, text)
    return match.group() if match else None

def extract_mobile_number(text, custom_regex=None):
    pattern = custom_regex or PHONE_REGEX
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_name(nlp_doc, matcher):
    patterns = [
        [{"POS": "PROPN"}, {"POS": "PROPN"}],
        [{"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}]
    ]
    matcher.add("NAME", patterns)
    matches = matcher(nlp_doc)
    for _, start, end in matches:
        span = nlp_doc[start:end]
        return span.text
    return None

# ========= 4. Skills Extraction ==========


def extract_skills(nlp_doc, noun_chunks, skills_file=None):
    # Load skills set
    skills_set = set(load_skills_from_file(skills_file) if skills_file else get_default_skills())
    found_skills = set()

    # Token-based check (exact match or partial match)
    tokens = [token.text.lower().strip() for token in nlp_doc if not token.is_stop and not token.is_punct]
    for token in tokens:
        for skill in skills_set:
            if skill in token:
                found_skills.add(skill)

    # Chunk-based check
    for chunk in noun_chunks:
        text = chunk.text.lower().strip()
        for skill in skills_set:
            if re.search(r'\b' + re.escape(skill) + r'\b', text):
                found_skills.add(skill)

    return sorted(found_skills)

def load_skills_from_file(path):
    if not path or not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

def get_default_skills():
    return set(HARD_SKILLS)

# ========= 5. Page Count ==========

def get_number_of_pages(file):
    try:
        pdf = PdfReader(file)
        return len(pdf.pages)
    except:
        return 1
