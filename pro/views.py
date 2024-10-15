from django.shortcuts import render
from .models import PersonalDetail, CodingProfile, Resume, Project, Skill, Certification, Internship, CoCurricular

def home(request):
    return render(request, 'home.html')

def personal_details(request):
    details = PersonalDetail.objects.all()
    return render(request, 'about.html', {'details': details})

def coding_profiles(request):
    profiles = CodingProfile.objects.all()
    return render(request, 'coding_profiles.html', {'profiles': profiles})

def resume(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})

def internships(request):
    internships = Internship.objects.all()
    return render(request, 'internships.html', {'internships': internships})

def co_curricular(request):
    activities = CoCurricular.objects.all()
    return render(request, 'co_curricular.html', {'activities': activities})
