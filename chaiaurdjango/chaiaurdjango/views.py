from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("Hello, world")


def contact(request):
    return HttpResponse("Hello, world")