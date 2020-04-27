from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def eNepal(request):
    context = {
        'title': "eNepal",
    }
    return render(request, 'course/eNepal.html', context)

@login_required(login_url='login')
def home(request):
    context = {
        'title': "Home",
    }
    return render(request, 'course/home.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'course/about.html', context)

def grade1(request):
    context = {
        'title': "Secondary",
    }
    return render(request, 'course/secondary.html', context)

def contact(request):
    return render(request, 'course/contact.html', {'title': "Contact"})
