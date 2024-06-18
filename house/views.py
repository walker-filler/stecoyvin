from django.shortcuts import render
from .models import House, Apartment, Land
# Create your views here.

def home(request):
    houses = House.objects.all()
    apartments = Apartment.objects.all()
    lands = Land.objects.all()
    return render(request, 'house/index.html', {'houses': houses, 'apartments': apartments, 'lands': lands})
