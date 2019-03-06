from django.shortcuts import render
from .models import Details, Skills, Language
# Create your views here.


def resume_display(request, resume_id):
    details = Details.objects.get(id=resume_id)
    skills = Skills.objects.filter(name=resume_id)
    language = Language.objects.filter(name=resume_id)
    context = {
        'details': details, 'skills': skills, 'language': language
    }
    return render(request, 'resume/profile.html', context)
