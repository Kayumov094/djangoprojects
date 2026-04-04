from django.urls import path 

# django kutubxonasining urls modulidan path degan funksiyani chaqirib oldim
from . import views
# home\views modulidan javob_qaytar deb yaratgan funksiyamizni chaqirib oldim

urlpatterns = [
    path('', views.home_page, name ='home')
]
# urlpatterns - bu royhat ko'rinishidagi maxsus o'zgaruvchi
# django serverga so'rov kelganda aynan shu nomli o'zgaruvchini qidiradi
# bu o'zgaruvchi loyihaning xaritasi 
# undagi barcha URL manzillar VIEWS dagi funksiyaga borish kerakligi yozilgan
# path() funksiyasi manzil va harakatni bo'glovchi funksiyasi 
# path(route, view, name)
# bunda route - brauzerda yozildigan manzil.Sizda bo‘sh qo‘shtirnoq '' turibdi. Bu — Bosh sahifa (domain nomi, masalan 127.0.0.1:8000/) degani
# view - yuqoridagi URL orqali viewga kelganda ishga tushadigan miyya 
# name bu manzilning laqabi. kelajakda kod manzilini yozib o'tirmasdan shu laqab bilan ishlatsa boladi
# degan o'zgaruvchi yaratdimmi? , path funkisyasi nima qiladi????
