import requests
from api.constants import JOB_ROLE_SKILLS_WEIGHT_MAP
from api.helpers import clean_text

def extract_top_skills(resume_text, top_n=5):
    resume_text = clean_text(resume_text)
    skill_scores = {}

    for role_skills in JOB_ROLE_SKILLS_WEIGHT_MAP.values():
        for skill, weight in role_skills.items():
            if skill.lower() in resume_text:
                skill_scores[skill] = skill_scores.get(skill, 0) + resume_text.count(skill.lower()) * weight

    sorted_skills = sorted(skill_scores.items(), key=lambda x: x[1], reverse=True)
    return [skill for skill, _ in sorted_skills[:top_n]]

# def fetch_jobs_from_remotive(skills, country="India"):
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    all_jobs = response.json().get("jobs", [])
    matching_jobs = []

    for job in all_jobs:
        job_title = job.get("title", "").lower()
        job_description = job.get("description", "").lower()
        job_country = job.get("candidate_required_location", "").lower()

        if country.lower() in job_country:
            for skill in skills:
                if skill.lower() in job_title or skill.lower() in job_description:
                    matching_jobs.append({
                        "title": job.get("title"),
                        "company": job.get("company_name"),
                        "location": job.get("candidate_required_location"),
                        "url": job.get("url")
                    })
                    break  # avoid duplicate matches for the same job

        if len(matching_jobs) >= 10:
            break

    return matching_jobs

# def fetch_jobs_from_remotive(target_role, skills=None, country="India", max_results=10):
    if not target_role:
        return []

    query = target_role.lower().replace(" ", "+")
    url = f"https://remotive.com/api/remote-jobs?search={query}"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    all_jobs = response.json().get("jobs", [])
    matching_jobs = []

    for job in all_jobs:
        job_title = job.get("title", "").lower()
        job_description = job.get("description", "").lower()
        job_country = job.get("candidate_required_location", "").lower()

        if country.lower() in job_country or "anywhere" in job_country:
            # Optional filtering using skills
            if skills:
                for skill in skills:
                    if skill.lower() in job_title or skill.lower() in job_description:
                        matching_jobs.append({
                            "title": job.get("title"),
                            "company": job.get("company_name"),
                            "location": job.get("candidate_required_location"),
                            "url": job.get("url")
                        })
                        break
            else:
                matching_jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "location": job.get("candidate_required_location"),
                    "url": job.get("url")
                })

        if len(matching_jobs) >= max_results:
            break

    return matching_jobs

# def fetch_jobs_from_remotive(target_role, skills=None, country="India", max_results=10):
    if not target_role:
        return []

    query = target_role.lower().replace(" ", "-")
    url = f"https://remotive.com/api/remote-jobs?category={query}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        all_jobs = response.json().get("jobs", [])
    except Exception as e:
        print(f"[ERROR] Remotive API call failed: {e}")
        return []

    matching_jobs = []
    for job in all_jobs:
        job_title = job.get("title", "").lower()
        job_description = job.get("description", "").lower()
        job_country = job.get("candidate_required_location", "").lower()

        if country.lower() in job_country or "anywhere" in job_country:
            if skills:
                for skill in skills:
                    if skill.lower() in job_title or skill.lower() in job_description:
                        matching_jobs.append({
                            "title": job.get("title"),
                            "company": job.get("company_name"),
                            "location": job.get("candidate_required_location"),
                            "url": job.get("url")
                        })
                        break
            else:
                matching_jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "location": job.get("candidate_required_location"),
                    "url": job.get("url")
                })

        if len(matching_jobs) >= max_results:
            break

    return matching_jobs

# import requests

# def fetch_jobs_from_remotive(target_role, skills=None, country="India", max_results=10):
    if not target_role:
        return []

    query = target_role.lower().replace(" ", "%20")
    url = f"https://remotive.com/api/remote-jobs?search={query}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        all_jobs = response.json().get("jobs", [])
    except Exception as e:
        print(f"[ERROR] Remotive API call failed: {e}")
        return []

    matching_jobs = []
    for job in all_jobs:
        job_title = job.get("title", "").lower()
        job_description = job.get("description", "").lower()
        job_country = job.get("candidate_required_location", "").lower()

        #if country.lower() in job_country or "anywhere" in job_country:
        if skills:
            for skill in skills:
                if skill.lower() in job_title or skill.lower() in job_description:                        matching_jobs.append({
                        "title": job.get("title"),
                        "company": job.get("company_name"),
                        "location": job.get("candidate_required_location"),
                        "url": job.get("url")
                })
                break
        else:
            matching_jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "url": job.get("url")
            })

        if len(matching_jobs) >= max_results:
            break

    return matching_jobs

import requests

def fetch_jobs_from_remotive(target_role, skills=None, country="India", max_results=10):
    if not target_role:
        print("[ERROR] No target role specified.")
        return []

    query = target_role.lower().replace(" ", "%20")
    url = f"https://remotive.com/api/remote-jobs?search={query}"
    print(f"[DEBUG] Query URL: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        all_jobs = response.json().get("jobs", [])
        print(f"[DEBUG] Total jobs fetched from API: {len(all_jobs)}")
    except Exception as e:
        print(f"[ERROR] Remotive API call failed: {e}")
        return []

    matching_jobs = []

    for job in all_jobs:
        print(f"🔍 Checking Job: {job.get('title')} at {job.get('company_name')}")
        job_title = job.get("title", "").lower()
        job_description = job.get("description", "").lower()

        if skills:
            for skill in skills:
                if skill.lower() in job_title or skill.lower() in job_description:
                    print(f"✅ Match found with skill: {skill}")
                    matching_jobs.append({
                        "title": job.get("title"),
                        "company": job.get("company_name"),
                        "location": job.get("candidate_required_location"),
                        "url": job.get("url")
                    })
                    break
        else:
            matching_jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "url": job.get("url")
            })

        if len(matching_jobs) >= max_results:
            break

    print(f"[DEBUG] Final matched jobs: {len(matching_jobs)}")
    return matching_jobs


def recommend_jobs(resume_text,target_role):
    top_skills = extract_top_skills(resume_text)
    jobs = fetch_jobs_from_remotive(target_role,top_skills, country="India")
    return jobs
