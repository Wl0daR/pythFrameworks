from django.shortcuts import render  
from .models import Car
from rest_framework import generics
from .serializers import CarSerializer

# Create your views here. 
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

def homeView(request):  
    cars = Car.objects.all()
    context = {'cars': cars}   
    return render(request, 'home.html', context)