from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.

def all_horcrux(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'horcrux/all_items.html', {'chais' : chais})

def about_them(request):
    return render(request, 'horcrux/about.html')

def worst(request):
    return render(request, 'horcrux/worst.html')
