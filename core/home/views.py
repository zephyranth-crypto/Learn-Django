from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'Name' : 'Tonny', 'Age' : 22},
        {'Name' : 'Robin', 'Age' : 15}

    ]
    return render(request, "index.html", context = {'peoples' : peoples, 'page' : 'Home'})

def about(request):
    context = {'page' : 'About-us'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)