from django.urls import path
from . import views

urlpatterns = [
    #localhost:3000/horcrux
    path('', views.all_horcrux, name="all_horcrux"),
    path('about/',views.about_them, name="about_them")
    #localhost:3000/horcrux/first
    #path('first/', views.first, name="first"),
    
]
