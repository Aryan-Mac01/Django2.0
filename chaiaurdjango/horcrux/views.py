from django.shortcuts import render

# Create your views here.

def all_horcrux(request):
    return render(request, 'horcrux/all_items.html')
