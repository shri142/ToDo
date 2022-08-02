from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("Hello World")

def kuchtoh(request):

    return HttpResponse("We are on main page")