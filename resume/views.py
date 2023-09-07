from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request, abb):
    try:
        role = Role.objects.get(abbreviation = abb)
    except ObjectDoesNotExist:
        # Handle the case where the Role does not exist
        role = None
    
    return render(request, 'resume/resume.html', {
        'role': role
    })

def test(request):
    return render(request, 'resume/test.html')
