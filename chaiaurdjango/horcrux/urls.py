from django.urls import path
from . import views

urlpatterns = [
    #localhost:3000/horcrux
    path('', views.all_horcrux, name="all_horcrux"),
    #localhost:3000/horcrux/first
    #path('first/', views.first, name="first"),
    
]
