import re
from difflib import SequenceMatcher
from collections import Counter
import textstat
import string
from spellchecker import SpellChecker
from .constants import (
    ACTION_WORDS, SOFT_SKILLS, HARD_SKILLS,
    COMMON_JOB_TITLES, BAD_PRONOUNS,
    FUZZY_HEADER_THRESHOLD
)
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Clean and normalize resume text for keyword matching:
    - Lowercase everything
    - Remove punctuation
    - Remove extra whitespace
    - Replace newlines/tabs with space
    """
    if not text:
        return ""
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r"[\n\r\t]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def fuzzy_header_found(header, text):
    """Check if header exists with fuzzy match in text."""
    return any(fuzzy_match(header, line) >= FUZZY_HEADER_THRESHOLD for line in text.split('\n'))

def fuzzy_match(a, b):
    return int(SequenceMatcher(None, a.lower(), b.lower()).ratio() * 100)

def count_action_verbs_in_bullets(bullets):
    count = 0
    for bullet in bullets:
        words = bullet.lower().split()
        if any(word in ACTION_WORDS for word in words[:3]):
            count += 1
    return count

def count_skills(text_tokens, skills_set):
    count = 0
    text_str = ' '.join(text_tokens)
    for skill in skills_set:
        if skill in text_str:
            count += 1
    return count

def detect_job_titles(text):
    doc = nlp(text)
    found_titles = set()
    lowered = text.lower()
    for title in COMMON_JOB_TITLES:
        if title in lowered:
            found_titles.add(title)
    return len(found_titles)

def detect_informal_or_filler(doc):
    informal_words = {"basically", "actually", "just", "very", "really", "stuff", "things"}
    buzzwords = {"synergy", "leverage", "streamline", "pivot", "bandwidth", "disrupt", "ecosystem"}
    count = 0
    for token in doc:
        if token.text.lower() in informal_words or token.text.lower() in buzzwords:
            count += 1
    return count

def get_readability_score(text):
    flesch = textstat.flesch_reading_ease(text)
    avg_sent_len = textstat.avg_sentence_length(text)
    passive_ratio = (
        textstat.passive_voice_percentage(text)
        if hasattr(textstat, "passive_voice_percentage")
        else 0
    )
    return flesch, avg_sent_len, passive_ratio

def get_spell_errors(doc):
    from spellchecker import SpellChecker
    spell = SpellChecker()
    words = [token.text for token in doc if token.is_alpha]
    errors = spell.unknown(words)
    error_counts = Counter(errors)
    return errors, error_counts
