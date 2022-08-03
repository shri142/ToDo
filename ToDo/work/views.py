from django.shortcuts import render , HttpResponse , redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):

    return HttpResponse("Hello World")

def kuchtoh(request):

    return HttpResponse("We are on kuch toh page")

def homepage(request):

    return HttpResponse("We are on home page")




