import os
import re
import tempfile
import spacy
from spacy.matcher import Matcher
from . import utils


class ResumeParser:
    def __init__(self, resume, skills_file=None, custom_regex=None):
        self.__skills_file = skills_file
        self.__custom_regex = custom_regex
        self.__resume = resume

        # Load NLP models
        self.__nlp_model = spacy.load('en_core_web_sm')
        self.__custom_nlp_model = spacy.load('en_core_web_sm')

        # Save resume to temp file
        ext = self.__get_file_extension(resume)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + ext) as tmp:
            tmp.write(resume.read())
            tmp_path = tmp.name

        self.__text_raw = utils.extract_text(tmp_path, '.' + ext)
        self.__text = ' '.join(self.__text_raw.split())

        # Run NLP
        self.__nlp = self.__nlp_model(self.__text)
        self.__custom_nlp = self.__custom_nlp_model(self.__text_raw)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__matcher = Matcher(self.__nlp_model.vocab)

        os.unlink(tmp_path)

        self.__details = self.__extract_details()

    def __get_file_extension(self, file):
        filename = getattr(file, 'filename', None)
        return filename.split('.')[-1] if filename else 'pdf'

    def __extract_details(self):
        details = {
            'name': None,
            'email': None,
            'mobile_number': None,
            'skills': None,
            'degree': None,
            'no_of_pages': None,
        }

        cust_ent = utils.extract_entities_with_custom_model(self.__custom_nlp)

        # --- Name Extraction ---
        try:
            name = cust_ent.get('Name', [None])[0]
            if not name:
                name = self.__extract_name_combined()
            details['name'] = name
        except:
            details['name'] = self.__extract_name_combined()

        # --- Email ---
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", self.__text)
        details['email'] = emails[0] if emails else None

        # --- Mobile ---
        details['mobile_number'] = utils.extract_mobile_number(self.__text, self.__custom_regex)

        # --- Skills ---
        skills_found = utils.extract_skills(self.__nlp, self.__noun_chunks, self.__skills_file)
        details['skills'] = list(set([s.lower() for s in skills_found]))

        # --- Pages ---
        details['no_of_pages'] = utils.get_number_of_pages(self.__resume)

        # --- Degrees ---
        try:
            degrees = cust_ent.get('Degree', [])
            if not degrees:
                degrees = utils.extract_degree_patterns(self.__text)
            details['degree'] = degrees
        except:
            details['degree'] = utils.extract_degree_patterns(self.__text)

        return details

    # def __extract_name_combined(self):
    #     # Blacklist common false positives
    #     blacklist = {"iris de", "john doe", "lorem ipsum"}

    #     # Check top lines first (your real name usually lives here)
    #     name = self.__extract_name_from_top_lines()
    #     if name and name.lower() not in blacklist:
    #         return name

    #     # Fall back to NER
    #     name = self.__extract_name_from_ner()
    #     if name and name.lower() not in blacklist:
    #         return name

    #     return None

    # def __extract_name_from_ner(self):
    #     for ent in self.__nlp.ents:
    #         if ent.label_ == "PERSON" and len(ent.text.split()) <= 4:
    #             name = ent.text.strip()
    #             if not any(char.isdigit() for char in name):
    #                 return name.title()
    #     return None

    # def __extract_name_from_top_lines(self, lines=5):
    #     raw_lines = self.__text_raw.strip().split('\n')[:lines]
    #     for line in raw_lines:
    #         clean = line.strip()
    #         if 2 <= len(clean.split()) <= 4 and not any(char.isdigit() for char in clean):
    #             return re.sub(r'\s+', ' ', clean).title()
    #     return None

    # def __extract_name_combined(self):
    #     # Expanded blacklist
    #     blacklist = {"iris de", "john doe", "lorem ipsum", "resume", "curriculum vitae"}

    #     # First: top lines
    #     name = self.__extract_name_from_top_lines()
    #     if name and name.lower() not in blacklist:
    #         return name

    #     # Second: Named Entity Recognition
    #     name = self.__extract_name_from_ner()
    #     if name and name.lower() not in blacklist:
    #         return name

    #     return None

    # def __extract_name_from_top_lines(self, lines=10):
    #     raw_lines = self.__text_raw.strip().split('\n')[:lines]
    #     unwanted_keywords = ["resume", "curriculum vitae", "cv", "email", "phone", "contact"]
        
    #     for line in raw_lines:
    #         clean = line.strip()
    #         if not clean or any(k in clean.lower() for k in unwanted_keywords):
    #             continue
    #         if 2 <= len(clean.split()) <= 4 and not any(char.isdigit() for char in clean):
    #             if clean.isupper():  # often full name in caps
    #                 return clean.title()
    #             return re.sub(r'\s+', ' ', clean).title()
    #     return None

    # def __extract_name_from_ner(self):
    #     # Prefer names in the top half of the document (heuristic)
    #     max_chars_to_check = len(self.__text) // 2
    #     for ent in self.__nlp.ents:
    #         if ent.label_ == "PERSON" and len(ent.text.split()) <= 4:
    #             if ent.start_char > max_chars_to_check:
    #                 continue  # skip lower part names
    #             name = ent.text.strip()
    #             if not any(char.isdigit() for char in name) and len(name) >= 4:
    #                 return name.title()
    #     return None
    # def __extract_name_combined(self):
    #     # Fallback order: Top lines → NER → Regex
    #     name = self.__extract_name_from_top_lines()
    #     if name:
    #         return name.strip()

    #     name = self.__extract_name_from_ner()
    #     if name:
    #         return name.strip()

    #     name = self.__extract_name_from_regex()
    #     if name:
    #         return name.strip()

    #     return None


    # def __extract_name_from_top_lines(self, lines=8):
    #     lines = self.__text_raw.strip().split('\n')[:lines]
    #     ignore_keywords = ['resume', 'curriculum', 'cv', 'email', 'phone', 'contact']

    #     for line in lines:
    #         clean = line.strip()
    #         if not clean or any(k in clean.lower() for k in ignore_keywords):
    #             continue

    #         # If it looks like a name
    #         if 2 <= len(clean.split()) <= 4 and clean == clean.title() and not any(char.isdigit() for char in clean):
    #             return clean
    #     return None


    # def __extract_name_from_ner(self):
    #     # Use spaCy to get PERSON entities near the top
    #     for ent in self.__nlp.ents:
    #         if ent.label_ == "PERSON":
    #             name = ent.text.strip()
    #             if 2 <= len(name.split()) <= 4 and not any(char.isdigit() for char in name):
    #                 return name.title()
    #     return None


    # def __extract_name_from_regex(self):
    #     # Try to grab capitalized words from the top lines
    #     lines = self.__text_raw.strip().split('\n')[:10]
    #     for line in lines:
    #         if any(char.isdigit() for char in line):
    #             continue
    #         words = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}', line)
    #         for w in words:
    #             if 2 <= len(w.split()) <= 4:
    #                 return w.strip()
    #     return None
    def __extract_name_combined(self):
        lines = self.__text_raw.strip().split('\n')[:6]

        ignore_keywords = ['resume', 'curriculum', 'cv', 'email', 'phone', 'contact']
        blacklist = {"john doe", "lorem ipsum", "sample name"}

        for line in lines:
            clean = line.strip()

            # Skip blank or unwanted lines
            if not clean or any(k in clean.lower() for k in ignore_keywords):
                continue

            # Skip if line has numbers
            if any(char.isdigit() for char in clean):
                continue

            # Accept if 2–4 words and all words are alphabetic
            words = clean.split()
            if 2 <= len(words) <= 4 and all(w.isalpha() for w in words):
                candidate = ' '.join(words)
                if candidate.lower() not in blacklist:
                    return candidate.title()  # Convert to proper case

        return None


    def get_extracted_data(self):
        return self.__details


# --- CLI testing mode ---
def resume_result_wrapper(resume_path):
    with open(resume_path, 'rb') as f:
        parser = ResumeParser(f)
        return parser.get_extracted_data()

if __name__ == '__main__':
    resumes_dir = 'resumes'
    resumes = [os.path.join(root, f) for root, _, files in os.walk(resumes_dir) for f in files]

    import multiprocessing as mp
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(resume_result_wrapper, resumes)

    for res in results:
        print(res)
