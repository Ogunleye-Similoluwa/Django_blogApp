from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, "hello.html")


def greet(request):
    return HttpResponse("Welcome to django")


def greet2(request):
    return render(request, 'ade.html')
