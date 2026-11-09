from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'Name' : 'Tonny', 'Age' : 22},
        {'Name' : 'Robin', 'Age' : 15}

    ]
    return render(request, "index.html", context = {'peoples' : peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")