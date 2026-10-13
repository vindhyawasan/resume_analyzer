from .skill_extractor import extract_skills
from .job_skill_extractor import extract_job_skill

def matching_resume_skill(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_job_skill(job_description)

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill.lower() in [s.lower() for s in resume_skills]:
            matched_skills.append(skill)

    for skill in job_skills:
        if skill.lower() not in [s.lower() for s in resume_skills]:
            missing_skills.append(skill)

    if len(job_skills) > 0:
        percentage = (len(matched_skills) / len(job_skills)) * 100
    else:
        percentage = 0

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "percentage": round(percentage, 2)
    }