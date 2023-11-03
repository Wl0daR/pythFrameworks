from django.shortcuts import render  
from .models import Car

# Create your views here. 

def homeView(request):  
    cars = Car.objects.all()
    context = {'cars': cars}   
    return render(request, 'home.html', context)