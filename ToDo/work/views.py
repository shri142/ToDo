from django.shortcuts import render , HttpResponse , redirect


# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def kuchtoh(request):

    return HttpResponse("We are on kuch toh page")

def homepage(request):

    return HttpResponse("We are on home page")









