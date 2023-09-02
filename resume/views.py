from django.shortcuts import render
from django.http import HttpResponse
from .models import roles_shortcut, Role

# Create your views here.
def index(request, abb):
    role = Role.objects.get(abb = abb)
    print(f"the projects are {role.works.all()}")
    
    return render(request, 'resume/resume.html', {
        'role': role
    })

def demo(request):
    return render(request, 'resume/demo.html')
