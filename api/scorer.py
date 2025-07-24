import re
import math
from collections import Counter
import textstat
import spacy

from .utils import (
    EMAIL_REGEX, PHONE_REGEX, LINKEDIN_REGEX, GITHUB_REGEX, PORTFOLIO_REGEX
)
from .constants import (
    HEADERS, HARD_SKILLS, SOFT_SKILLS, BAD_PRONOUNS,
    MAX_HEADER_SCORE, MAX_ACTION_VERB_SCORE, MAX_SKILLS_SCORE,
    MAX_CONTACT_SCORE, MAX_READABILITY_SCORE, MAX_SPELLING_SCORE,
    MAX_PRONOUN_SCORE, MAX_WORDCOUNT_SCORE, MAX_JOBTITLE_SCORE,
    MAX_NEGATIVE_PENALTY
)
from .helpers import (
    fuzzy_header_found,
    count_action_verbs_in_bullets,
    count_skills,
    detect_job_titles,
    detect_informal_or_filler,
    get_readability_score,
    get_spell_errors
)

nlp = spacy.load("en_core_web_sm")

def get_resume_score(resume_text: str) -> int:
    score = 0
    text_lower = resume_text.lower()
    doc = nlp(resume_text)
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]

    # 1. Header Detection
    headers_found = sum(1 for header in HEADERS if fuzzy_header_found(header, text_lower))
    score += min(headers_found * 2, MAX_HEADER_SCORE)

    # 2. Action Verbs in Bullet Points
    bullet_points = re.findall(r"(?:•|-|\*)\s?(.*)", resume_text)
    action_verb_count = count_action_verbs_in_bullets(bullet_points)
    score += min(action_verb_count * 2, MAX_ACTION_VERB_SCORE)

    # 3. Skills Detection
    soft_skill_count = count_skills(tokens, SOFT_SKILLS)
    hard_skill_count = count_skills(tokens, HARD_SKILLS)
    total_skills = soft_skill_count + hard_skill_count
    skills_score = min(MAX_SKILLS_SCORE, int(5 * math.log1p(total_skills)))
    score += skills_score

    # 4. Contact Info Presence
    contact_points = 0
    if re.search(EMAIL_REGEX, resume_text): contact_points += 3
    if re.search(PHONE_REGEX, resume_text): contact_points += 3
    contact_points += 2 if re.search(LINKEDIN_REGEX, resume_text) else 0
    contact_points += 2 if re.search(GITHUB_REGEX, resume_text) else 0
    contact_points += 2 if re.search(PORTFOLIO_REGEX, resume_text) else 0
    score += min(contact_points, MAX_CONTACT_SCORE)

    # 5. Readability
    flesch, avg_sent_len, passive_ratio = get_readability_score(resume_text)
    if flesch > 65 and avg_sent_len < 20 and passive_ratio < 5:
        score += MAX_READABILITY_SCORE
    elif flesch > 50:
        score += int(MAX_READABILITY_SCORE * 0.7)
    else:
        score += int(MAX_READABILITY_SCORE * 0.4)

    # 6. Spelling Quality
    errors, error_counts = get_spell_errors(doc)
    error_ratio = len(errors) / max(len([t for t in doc if t.is_alpha]), 1)
    repeated_errors = sum(1 for err, cnt in error_counts.items() if cnt > 1)
    if error_ratio < 0.01 and repeated_errors == 0:
        score += MAX_SPELLING_SCORE
    elif error_ratio < 0.02:
        score += int(MAX_SPELLING_SCORE * 0.7)
    elif error_ratio < 0.04:
        score += int(MAX_SPELLING_SCORE * 0.4)

    # 7. Personal Pronoun Check
    if not any(pronoun in text_lower.split() for pronoun in BAD_PRONOUNS):
        score += MAX_PRONOUN_SCORE

    # 8. Word Count Scoring
    wc = len(tokens)
    if 350 <= wc <= 700:
        score += MAX_WORDCOUNT_SCORE
    elif 250 <= wc < 350 or 700 < wc <= 900:
        score += int(MAX_WORDCOUNT_SCORE * 0.5)
    else:
        score += int(MAX_WORDCOUNT_SCORE * 0.2)

    # 9. Job Title Detection
    job_title_count = detect_job_titles(text_lower)
    score += min(job_title_count * 3, MAX_JOBTITLE_SCORE)

    # 10. Filler Word Penalty
    informal_count = detect_informal_or_filler(doc)
    score -= min(informal_count * 2, MAX_NEGATIVE_PENALTY)

    ans= max(0, min(100, score))
        
    return min(99,ans+35)
