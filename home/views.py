from django.shortcuts import render 
# django kutubxonasining shortcuts modulidan render funsiyasini chaqirib oldim
from django.http import HttpResponse
# django kutubxonasining http modulidan HttpResponse funksiyasini chaqirib oldim
# home\views.py ikki asosga quriladi:
# Class-based View - class asosida 
# Function-Based View - def funksiya assosida 

# Asosiy qismga o'tamiz 
def javob_qaytar(request):
    return render(request, 'home.html')
