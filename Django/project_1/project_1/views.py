from django.http import HttpResponse

def Home(request):
    return HttpResponse("the home page.")

def About(request):
    return HttpResponse("the about page.")