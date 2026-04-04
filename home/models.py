from django.db import models
from about.models import Xodim

# Create your models here.


class Loyiha(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Loyiha nomi")
    tavsifi = models.TextField(max_length=1000, verbose_name = "Loyiha tavsifi")
    yili = models.IntegerField(verbose_name = "Bajarilgan yili")
    hudud = models.CharField(max_length=50, verbose_name = "Tegishli hudud")
    davlat = models.CharField(max_length=50, verbose_name="Tegishli davlat")
    masul_xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, verbose_name = "Loyiha uchun mas'ul xodim")

    def __str__(self):
        return self.nomi
    



# class Skopx:
#     pass

# class home:
#     pass

# class Loyiha:
#     def __init__(self, nomi, tavsifi, yili, hudud, davlat, xodim_obyekti):
#         self.nomi = nomi
#         self.tavsifi = tavsifi
#         self.yili = yili
#         self.hudud = hudud
#         self.davlat = davlat
#         self.masul_xodim = xodim_obyekti
#     def __str__(self):
#         return (f"Loyiha nomi: {self.nomi};\n"
#                 f"Description Project:{self.tavsifi};\n"
#                 f"Bajarilgan yili: {self.yili};\n"
#                 f"Tegishli hudud: {self.hudud};\n"
#                 f"Tegishli davlat: {self.davlat};\n"
#                 f"Ma'sul xodim: {self.masul_xodim};\n")
    
#     def __repr__(self):
#         return f"Loyiha('{self.nomi}', {self.yili})"
    
# loyiha1 = Loyiha("Minim Backend", "Minim design Agency Data infrastructure", 2026, "Toshkent", "O'zbekiston", xodim1)
# loyiha2 = Loyiha("Researching Market", "Raqobatchilarni o'rganib chiqish", 2026, "Fergana", "O'zbekiston", xodim2)
# loyiha3 = Loyiha("Skopx HR strategy", "Kompaniyaning HR stategiyasi", 2026, "Toshkent", "Japan", xodim3)




