from django.db import models

# Create your models 
class Resume(models.Model):
    file = models.FileField(upload_to="resumes")
    extract_text = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class Job(models.Model):
    title = models.TextField(max_length=200)
    company = models.TextField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.TextField(max_length=100, unique=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Analyze(models.Model):
    resume = models.ForeignKey(
        Resume,
        models.CASCADE
    )
    job = models.ForeignKey(
        Job,
        models.CASCADE
    )

    score = models.FloatField()
    matched_skills = models.TextField(blank=True)
    missing_skills = models.TextField(blank=True)
    suggestion = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True) 