import re
from analyzer.models import Skill

def extract_job_skill(description):
    skills = Skill.objects.all()

    found_skills = []
    for skill in skills:
        if re.search(
            r"\b" + re.escape(skill.name) + r"\b",
            description,
            re.IGNORECASE
        ):
            found_skills.append(skill.name)
    return found_skills