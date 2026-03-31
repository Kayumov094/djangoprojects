from django.shortcuts import render
#django kutubxonasidan shortcuts moduli ichidan render funksiyasini chaqirib oldim 
from django.http import HttpResponse
# django kutubxonasida http moduli ichidan HttpResponse funksiyasini chaqirib oldim

# About app uchun create function named: about_uchun_javob_qaytar
# agar shu nomli funksiyaga murojaat qilinsa "Welocome to about " degan javob qayatardi.
#Tayyor bolgan view ni urlsga birlashtiraman
# Create your views here.
def about_uchun_javob_qaytar(request):
    return render(request, 'about.html')
         