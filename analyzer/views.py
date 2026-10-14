
from django.shortcuts import render
from .form import ResumeForm
from .utils import extract_text_from_pdf
from .skill_extractor import extract_skills
from .models import Analyze, Job
from .matching import matching_resume_skill


def index(request):

    jobs = Job.objects.all()

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            job_id = request.POST.get("job")

            if not job_id:
                return render(
                    request,
                    "index.html",
                    {
                        "form": form,
                        "jobs": jobs,
                        "error": "Please select a job."
                    }
                )

            resume = form.save()

            text = extract_text_from_pdf(resume.file)
            skills = extract_skills(text)

            resume.extract_text = text
            resume.save()

            job = Job.objects.get(id=job_id)

            result = matching_resume_skill(
                text,
                job.description
            )

            analysis = Analyze.objects.create(
                resume=resume,
                job=job,
                score=result["percentage"],
                matched_skills=", ".join(
                    result["matched_skills"]
                ),
                missing_skills=", ".join(
                    result["missing_skills"]
                ),
                suggestion=""
            )

            return render(
                request,
                "index.html",
                {
                    "form": ResumeForm(),
                    "resume": resume,
                    "skills": skills,
                    "jobs": jobs,
                    "analysis": analysis
                }
            )

        else:
            return render(
                request,
                "index.html",
                {
                    "form": form,
                    "jobs": jobs
                }
            )

    else:
        form = ResumeForm()

    return render(
        request,
        "index.html",
        {
            "form": form,
            "jobs": jobs
        }
    )
