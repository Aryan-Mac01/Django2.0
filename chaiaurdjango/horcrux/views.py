from django.shortcuts import render

# Create your views here.

def all_horcrux(request):
    return render(request, 'horcrux/all_items.html')

def about_them(request):
    return render(request, 'horcrux/about.html')

def worst(request):
    return render(request, 'horcrux/worst.html')
