from django.shortcuts import render
from .form import ResumeForm
from .utils import extract_text_from_pdf
from .skill_extractor import extract_skills

def index(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save()
            text = extract_text_from_pdf(resume.file)
            skills = extract_skills(text)
            resume.extract_text = text
            resume.save()
            print("Extracted Skills:", skills)
            return render(request,
                          "index.html",{
                              "form" : ResumeForm(),
                              "resume" : resume,
                              "skills" : skills
                          })
        elif form.errors:
            return render(request,
                          "index.html",{
                              "form" : form
                          })
        
        else:
            form = ResumeForm() 
            return render(request,
                          "index.html",{
                              "form" : form
                          })
    return render(request, "index.html")

# Create your views here.
