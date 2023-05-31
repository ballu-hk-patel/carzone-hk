from django.shortcuts import render
from pages.models import Team

# Create your views here.
def home(request):
    teams= Team.objects.all()
    data={
        'teams': teams,
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams= Team.objects.all()
    data={
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)

def contanct(request):
    return render(request, 'pages/contact.html')

def service(request):
    return render(request, 'pages/service.html')

# def cars(request):
#     return pass
