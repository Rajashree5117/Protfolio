from django.db import models

class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

class CodingProfile(models.Model):
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()

class Resume(models.Model):
    resume_pdf = models.FileField(upload_to='resumes/')
    resume_doc = models.FileField(upload_to='resumes/')

class Project(models.Model):
    title = models.CharField(max_length=100)
    github_link = models.URLField()
    video_overview = models.URLField()

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()  # e.g., 1 to 10 scale

class Certification(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='certifications/')
    doc_file = models.FileField(upload_to='certifications/')

class Internship(models.Model):
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    internship_pdf = models.FileField(upload_to='internships/')
    internship_doc = models.FileField(upload_to='internships/')

class CoCurricular(models.Model):
    activity_name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='co_curricular/')
    doc_file = models.FileField(upload_to='co_curricular/')
    ppt_file = models.FileField(upload_to='co_curricular/')
    image = models.ImageField(upload_to='co_curricular/')
