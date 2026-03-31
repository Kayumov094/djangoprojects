from django.urls import path 
from .views import about_uchun_javob_qaytar

urlpatterns = [
    path('', about_uchun_javob_qaytar, name = 'about')
]