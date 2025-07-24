# # import re
# # from api.constants import JOB_ROLE_SKILLS_WEIGHT_MAP, COURSE_CATALOG
# # from api.helpers import clean_text

# # def count_weighted_skill_frequency(text, weighted_skills):
# #     text = clean_text(text)
# #     score = 0
# #     for skill, weight in weighted_skills.items():
# #         # Use word boundaries for accurate match
# #         pattern = r"\b" + re.escape(skill.lower()) + r"\b"
# #         matches = re.findall(pattern, text)
# #         score += len(matches) * weight
# #     return score

# # def predict_job_role(text):
# #     max_score = 0
# #     predicted_role = None
# #     for role, skills_weight_map in JOB_ROLE_SKILLS_WEIGHT_MAP.items():
# #         score = count_weighted_skill_frequency(text, skills_weight_map)
# #         if score > max_score:
# #             max_score = score
# #             predicted_role = role
# #     return predicted_role, max_score

# # def recommend_missing_skills(text, predicted_role):
# #     text = clean_text(text)
# #     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role, {})
# #     missing = []
# #     for skill in weighted_skills:
# #         pattern = r"\b" + re.escape(skill.lower()) + r"\b"
# #         if not re.search(pattern, text):
# #             missing.append(skill)
# #     return missing

# # #def recommend_courses_for_skills(missing_skills, predicted_role):
# #     #weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role, {})
# #     ## Sort missing skills by importance (weight)
# #     #missing_skills.sort(key=lambda x: weighted_skills.get(x, 0), reverse=True)

# #     #recommended_courses = []
# #     #for skill in missing_skills:
# #         #course_url = COURSE_CATALOG.get(skill.lower())
# #         #if course_url:
# #         #    recommended_courses.append((skill, course_url))
# #         #if len(recommended_courses) >= 5:
# #         #    break
# #     #return recommended_courses

# # #from constants import JOB_ROLE_SKILLS_WEIGHT_MAP, COURSE_CATALOG

# # def recommend_courses_for_skills(missing_skills, predicted_role):
# #     # Get skill weights for this role
# #     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})

# #     # Sort missing skills by importance (descending weight)
# #     missing_skills.sort(key=lambda x: weighted_skills.get(x.lower(), 0), reverse=True)

# #     recommended_courses = {}
# #     count = 0

# #     for skill in missing_skills:
# #         course_entries = COURSE_CATALOG.get(skill.lower(), [])
# #         #print(f"Skill: {skill}, Course: {COURSE_CATALOG.get(skill.lower())}")
# #         if course_entries:
# #             recommended_courses[skill] = course_entries
# #             count += 1
# #             #recommended_courses.append({
# #             #    "skill": skill,
# #             #    "courses": course_entries  # Already a list of {name, url}
# #             #})
            
# #         if count >= 5:  # Limit total to 5 skill recommendations
# #             break

# #     return recommended_courses


# # #def recommend_skills_and_courses(text):
# # #    predicted_role, confidence = predict_job_role(text)
# # #    if not predicted_role:
# # #        return {"error": "Could not confidently predict role"}

# # #    missing_skills = recommend_missing_skills(text, predicted_role)
# # #    recommended_courses = recommend_courses_for_skills(missing_skills, predicted_role)
# # #
# #  #   return {
# #   #      "predicted_role": predicted_role,
# #    #     "missing_skills": missing_skills,
# #     #    "recommended_courses": recommended_courses,
# #      #   "confidence_score": round(confidence, 2)
# #     #}

# # def recommend_skills_and_courses(text, target_role=None):
# #     if not target_role:
# #         predicted_role, confidence = predict_job_role(text)
# #         if not predicted_role:
# #             return {"error": "Could not confidently predict role"}

# #         target_role = predicted_role
# #         confidence_score = round(confidence, 2)
# #     else:
# #         confidence_score = 1.0  # full confidence since user chose it manually

# #     missing_skills = recommend_missing_skills(text, target_role)
# #     recommended_courses = recommend_courses_for_skills(missing_skills, target_role)

# #     return {
# #         "predicted_role": target_role,
# #         "missing_skills": missing_skills,
# #         "recommended_courses": recommended_courses,
# #         "confidence_score": confidence_score
# #     }


# import re
# from api.constants import JOB_ROLE_SKILLS_WEIGHT_MAP, COURSE_CATALOG
# from api.helpers import clean_text

# def count_weighted_skill_frequency(text, weighted_skills):
#     text = clean_text(text)
#     score = 0
#     for skill, weight in weighted_skills.items():
#         pattern = r"\b" + re.escape(skill.lower()) + r"\b"
#         matches = re.findall(pattern, text.lower())
#         score += len(matches) * weight
#     return score

# def predict_job_role(text):
#     max_score = 0
#     predicted_role = None
#     for role, skills_weight_map in JOB_ROLE_SKILLS_WEIGHT_MAP.items():
#         score = count_weighted_skill_frequency(text, skills_weight_map)
#         if score > max_score:
#             max_score = score
#             predicted_role = role
#     return predicted_role, max_score

# def recommend_missing_skills(text, predicted_role):
#     text_cleaned = clean_text(text).lower()
#     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
#     extracted = set(re.findall(r'\b\w+\b', text_cleaned))

#     missing = []
#     for skill in weighted_skills:
#         tokens = set(skill.lower().split())
#         if not tokens.issubset(extracted):
#             missing.append(skill)

#     return missing

# def recommend_courses_for_skills(missing_skills, predicted_role):
#     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
#     missing_skills.sort(key=lambda x: weighted_skills.get(x.lower(), 0), reverse=True)

#     recommended_courses = {}
#     count = 0

#     for skill in missing_skills:
#         course_entries = COURSE_CATALOG.get(skill.lower(), [])
#         if course_entries:
#             recommended_courses[skill] = course_entries
#             count += 1
#         if count >= 5:
#             break

#     return recommended_courses

# def recommend_skills_and_courses(text, target_role=None):
#     if not target_role:
#         predicted_role, confidence = predict_job_role(text)
#         if not predicted_role:
#             return {"error": "Could not confidently predict role"}
#         target_role = predicted_role
#         confidence_score = round(confidence, 2)
#     else:
#         confidence_score = 1.0  # Manual selection

#     missing_skills = recommend_missing_skills(text, target_role)
#     recommended_courses = recommend_courses_for_skills(missing_skills, target_role)

#     return {
#         "predicted_role": target_role,
#         "missing_skills": missing_skills,
#         "recommended_courses": recommended_courses,
#         "confidence_score": confidence_score
#     }

import re
from api.constants import JOB_ROLE_SKILLS_WEIGHT_MAP, COURSE_CATALOG
from api.helpers import clean_text

# for skill in list(COURSE_CATALOG.keys()):
#     if isinstance(COURSE_CATALOG[skill], str):
#         COURSE_CATALOG[skill] = [COURSE_CATALOG[skill]]

def get_role_key_insensitive(role_name):
    for role in JOB_ROLE_SKILLS_WEIGHT_MAP.keys():
        if role.lower() == role_name.lower():
            return role
    return None


def count_weighted_skill_frequency(text, weighted_skills):
    text = clean_text(text).lower()
    score = 0
    for skill, weight in weighted_skills.items():
        if skill.lower() in text:
            score += text.count(skill.lower()) * weight
    return score

def predict_job_role(text):
    max_score = 0
    predicted_role = None
    for role, skills_weight_map in JOB_ROLE_SKILLS_WEIGHT_MAP.items():
        score = count_weighted_skill_frequency(text, skills_weight_map)
        if score > max_score:
            max_score = score
            predicted_role = role
    return predicted_role, max_score

# def recommend_missing_skills(text, predicted_role):
#     cleaned_text = clean_text(text).lower()
#     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
#     missing = []

#     # for skill in weighted_skills:
#     #     if skill.lower() not in text:
#     #         missing.append(skill)
#     for skill in weighted_skills:
#         pattern = r"\b" + re.escape(skill.lower()) + r"\b"
#         if not re.search(pattern, cleaned_text):
#             missing.append(skill)
#     return missing
def recommend_missing_skills(text, predicted_role):
    cleaned_text = clean_text(text).lower()
    role_key = get_role_key_insensitive(predicted_role)
    if not role_key:
        return []

    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP[role_key]
    missing_skills = []

    for skill in weighted_skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if not re.search(pattern, cleaned_text):
            missing_skills.append(skill)

    return missing_skills

# def recommend_courses_for_skills(missing_skills, predicted_role):
#     # Get skill weights for this role
#     weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})

#     # Sort missing skills by importance (descending weight)
#     missing_skills.sort(key=lambda x: weighted_skills.get(x.lower(), 0), reverse=True)

#     recommended_courses = {}
#     count = 0

#     for skill in missing_skills:
#         course_entries = COURSE_CATALOG.get(skill.lower(), [])
#         if course_entries:
#             recommended_courses[skill] = course_entries
#             count += 1
#         if count >= 5:  # Limit to 5
#             break

#     return recommended_courses
# def recommend_courses_for_skills(missing_skills, predicted_role):
    role_key = get_role_key_insensitive(predicted_role)
    if not role_key:
        return {}

    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP[role_key]

    # Sort missing skills by descending weight (0 if not found)
    sorted_missing = sorted(
        missing_skills,
        key=lambda skill: weighted_skills.get(skill.lower(), 0),
        reverse=True
    )

    recommended_courses = {}
    count = 0

    for skill in sorted_missing:
        skill_lower = skill.lower()
        course_entries = COURSE_CATALOG.get(skill_lower, [])
        if course_entries:
            recommended_courses[skill] = course_entries
            count += 1
        if count >= 5:
            break

    return recommended_courses
# def recommend_missing_skills(resume_skills, predicted_role):
    """
    Identify important missing skills for the predicted role.

    Args:
        resume_skills (set or list): Skills extracted from the resume.
        predicted_role (str): Job role predicted from resume content.

    Returns:
        List[str]: Top 5 important missing skills for the role.
    """
    if not resume_skills or not predicted_role:
        return []

    required_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
    resume_skills_lower = set(skill.lower() for skill in resume_skills)

    # Get all required skills not in resume
    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in resume_skills_lower
    ]

    # Sort by importance (descending weight)
    missing_skills.sort(
        key=lambda skill: required_skills.get(skill.lower(), 0),
        reverse=True
    )

    return missing_skills[:5]  # Return top 5 missing


# def recommend_courses_for_skills(missing_skills, predicted_role):
    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
    missing_skills.sort(key=lambda x: weighted_skills.get(x.lower(), 0), reverse=True)

    recommended_courses = {}
    count = 0

    for skill in missing_skills:
        course_entries = COURSE_CATALOG.get(skill.lower(), [])
        if course_entries:
            recommended_courses[skill] = course_entries
            count += 1
        if count >= 5:
            break

    return recommended_courses

# def recommend_courses_for_skills(missing_skills, predicted_role):
    """
    Recommend top courses based on missing important skills for a role.

    Args:
        missing_skills (List[str]): List of important missing skills.
        predicted_role (str): The job role being evaluated.

    Returns:
        Dict[str, List[str]]: Mapping of missing skill to recommended course URLs.
    """
    recommended_courses = {}
    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})

    # Sort missing skills by their weight (importance)
    missing_skills.sort(key=lambda x: weighted_skills.get(x.lower(), 0), reverse=True)

    count = 0
    for skill in missing_skills:
        course_links = COURSE_CATALOG.get(skill.lower(), [])
        if course_links:
            recommended_courses[skill] = course_links
            count += 1
        if count >= 5:  # Recommend max 5 course groups
            break

    return recommended_courses

# def recommend_courses_for_skills(missing_skills, predicted_role):
    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})
    
    # Sort missing skills by importance (descending weight)
    sorted_missing_skills = sorted(
        missing_skills,
        key=lambda skill: weighted_skills.get(skill.lower(), 0),
        reverse=True
    )

    recommended_courses = {}
    total_courses = 0
    max_courses = 5  # Limit to 5 total course links

    for skill in sorted_missing_skills:
        raw_courses = COURSE_CATALOG.get(skill.lower(), [])

        # Ensure it's a list
        if isinstance(raw_courses, str):
            raw_courses = [raw_courses]

        # Filter valid strings only (prevent error from bad data)
        course_entries = [course for course in raw_courses if isinstance(course, str)]

        if course_entries:
            # Trim to avoid exceeding max limit
            space_left = max_courses - total_courses
            trimmed_courses = course_entries[:space_left]
            recommended_courses[skill] = trimmed_courses
            total_courses += len(trimmed_courses)

        if total_courses >= max_courses:
            break

    return recommended_courses

def recommend_courses_for_skills(missing_skills, predicted_role):
    weighted_skills = JOB_ROLE_SKILLS_WEIGHT_MAP.get(predicted_role.lower(), {})

    sorted_missing_skills = sorted(
        missing_skills,
        key=lambda skill: weighted_skills.get(skill.lower(), 0),
        reverse=True
    )

    recommended_courses = {}
    total_courses = 0
    max_courses = 5

    for skill in sorted_missing_skills:
        course_links = COURSE_CATALOG.get(skill.lower(), [])

        # Ensure it's a list
        if isinstance(course_links, str):
            course_links = [course_links]
        elif not isinstance(course_links, list):
            continue

        # Only accept up to remaining courses
        space_left = max_courses - total_courses
        trimmed = course_links[:space_left]

        if trimmed:
            recommended_courses[skill] = trimmed
            total_courses += len(trimmed)

        if total_courses >= max_courses:
            break

    return recommended_courses


def recommend_skills_and_courses(text, target_role=None):
    if not target_role:
        predicted_role, confidence = predict_job_role(text)
        if not predicted_role:
            return {"error": "Could not confidently predict role"}
        target_role = predicted_role
        confidence_score = round(confidence, 2)
    else:
        confidence_score = 1.0

    missing_skills = recommend_missing_skills(text, target_role)
    recommended_courses = recommend_courses_for_skills(missing_skills, target_role)

    return {
        "predicted_role": target_role,
        "missing_skills": missing_skills,
        "recommended_courses": recommended_courses,
        "confidence_score": confidence_score
    }
