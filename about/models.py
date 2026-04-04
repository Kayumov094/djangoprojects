from django.db import models

# Create your models here.

class Xodim(models.Model):
    lavozim = models.CharField(max_length=50, verbose_name="Lavozimi")
    ism = models.CharField(max_length=50, verbose_name = "Ismi")
    familiya = models.CharField(max_length=50, verbose_name = "Familiya")
    tajriba_yil = models.IntegerField(verbose_name = "Tajribasi (yil)")

    def __str__(self):
        return f"{self.familiya} {self.ism} ({self.lavozim})"
    


class Kontakt(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, verbose_name = Xodim)
    tel_nomer = models.CharField(max_length=20, verbose_name = "Telefon raqami")

    def __str__(self):
        return f"{self.xodim.lavozim} - {self.xodim.familiya} {self.xodim.ism}: {self.tel_nomer}"





# class Kontakt:
#     def __init__(self, xodim_obyekti, tel_nomer):
#         self.lavozim = xodim_obyekti.lavozim
#         self.ism = xodim_obyekti.ism
#         self.tel_nomer = tel_nomer
        

#     def __str__(self):
#         return (f"Lavozimi: {self.lavozim}\n"
#                 f"Ismi: {self.ism}\n"
#                 f"Telefon raqami: {self.tel_nomer}\n"
#         )
# class Xodim:
#     def __init__(self,lavozim, ism, familiya, tajriba_yil):
#         self.lavozim = lavozim
#         self.ism = ism
#         self.familiya = familiya
#         self.tajriba_yil = tajriba_yil
#         self.bajarilgan_loyihalar = []
#     def __str__(self):
#         loyihalar = ", ".join(self.bajarilgan_loyihalar)
#         if self.bajarilgan_loyihalar:
#              return f"Lavozimi: {self.lavozim},\nIsmi: {self.ism},\nFamiliyasi: {self.familiya},\nYillik tajribasi: {self.tajriba_yil},\nIshtirok etgan loyihalar:{loyihalar} "
#         else:
#             "Hozircha mavjud emas"
       
    
#     def loyihani_bajar(self, nomi):
#         self.bajarilgan_loyihalar.append(nomi)
#         return 
#     def loyihalarni_sana(self):
#         return len(self.bajarilgan_loyihalar)


# xodim1 = Xodim("Direktor", "Arslonbek", "Qayumov", 8 )
# xodim2 = Xodim("Analitik", "Sevara", "Xomidova", 12)
# xodim3 = Xodim("HR direktor","Gulyora", "Qayumova", 8)
# xodim1.loyihani_bajar("Minim Backend")
# xodim2.loyihani_bajar("Researching Market")
# xodim3.loyihani_bajar("Skopx HR strategy")
# xodim1.loyihani_bajar("Mountain Backend")

# # print(xodim1)
# # print(30*"*")
# # print(xodim2)
# # print(30*"*")
# # print(xodim3)
# # print(xodim1.loyihalarni_sana())
# # print(xodim2.loyihalarni_sana())
# # print(xodim3.loyihalarni_sana())


# class Blog:
#     def __init__(self,nomi, tavsifi, yili):
#         self.nomi = nomi
#         self.tavsifi = tavsifi
#         self.yili = int(yili)
#     def __gt__(self, boshqa_maqola): # Solishtirish imkonini beruvchi dunder method
#         return self.yili > boshqa_maqola.yili
#     def __str__(self): # print qilganda chiroyli qiliib chiqarib beruvchi dunder method
#         return f"Maqola nomi: {self.nomi};\nQisqacha tavsifi: {self.tavsifi};\nChop qilingan yili: {self.yili}"
    
# maqola1 = Blog("Data analitika nima?", "Analitikaga kirish", "2026")
# maqola2 = Blog("Data muhandisligi nima?", "Data muhadisligiga kirish", "2024")
# maqola3 = Blog("Data science nima?", "Data science ga  kirish", "2025")

# # print("*"* 30)
# # print(maqola1)
# # print("*"* 30)
# # print(maqola2)
# # print("*"* 30)
# # print(maqola3)

# # maqolalar = [maqola1, maqola2, maqola3]
# # maqolalar.sort()
# # print("Maqolalarning tartiblangan royhati:")
# # for i in maqolalar:
# #     print(i)
    


# tel1 = Kontakt(xodim1, "+998-90-577-35-23")
# tel3 = Kontakt(xodim2, "+998-97-595-33-63")
# tel2 = Kontakt(xodim3, "+998-90-536-48-80")
 

