from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Home(request):
    return HttpResponse("the home page.")

def About(request):
    return HttpResponse("the about page.")