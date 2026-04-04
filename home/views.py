from django.shortcuts import render
from .models import Loyiha
  

def home_page(request):
    loyihalar = Loyiha.objects.all()

    context = {
        'loyihalar': loyihalar
    }   
    return render(request, 'home.html', context)
