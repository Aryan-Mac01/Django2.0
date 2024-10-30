from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.

def all_horcrux(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'horcrux/all_items.html', {'chais' : chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'horcrux/chai_detail.html', {'chais': chais})

def about_them(request):
    return render(request, 'horcrux/about.html')

def worst(request):
    return render(request, 'horcrux/worst.html')
