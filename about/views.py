from django.shortcuts import render
#django kutubxonasidan shortcuts moduli ichidan render funksiyasini chaqirib oldim 
from .models import Kontakt, Xodim

# funksiya yordamida DB dan Xodim va Kontakt degan table larni chqirib oldim
def about_page(request):
    xodimlar = Xodim.objects.all()
    kontaktlar = Kontakt.objects.all()

# Kelgan barcha malumotlarni context degan qutiga soldim
    context = {
        'xodimlar': xodimlar,
        'kontaktlar': kontaktlar
    }
# Qutini about.html ga jonataman
    return render(request, 'about.html', context)
        
       