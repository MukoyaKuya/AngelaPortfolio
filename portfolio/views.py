from django.shortcuts import render
from .models import Profile, Skill, Experience, Education, Certification, Achievement

def index(request):
    profile = Profile.objects.first()
    # Group skills by category for better display
    analytics_skills = Skill.objects.filter(category='ANALYTICS')
    engineering_skills = Skill.objects.filter(category='ENGINEERING')
    bi_skills = Skill.objects.filter(category='BI')
    
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    achievements = Achievement.objects.all()
    
    context = {
        'profile': profile,
        'analytics_skills': analytics_skills,
        'engineering_skills': engineering_skills,
        'bi_skills': bi_skills,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
        'achievements': achievements,
    }
    return render(request, 'portfolio/index.html', context)
