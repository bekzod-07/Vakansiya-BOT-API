from django.db import models

class BaseTumani(models.Model):
    INN = models.CharField(max_length=50)
    COATO = models.CharField(max_length=50)
    TASHKILOT_NOMI = models.TextField()
    OKED = models.CharField(max_length=30)
    COOGU = models.CharField(max_length=30)
    BOLIM_NOMI = models.TextField()
    LAVOZIM = models.TextField()
    BOSH_ISH_ORIN_BIRLIGI = models.CharField(max_length=10)
    NSKZ = models.CharField(max_length=30)
    TELERAQAM1 = models.CharField(max_length=30)
    TELERAQAM2 = models.CharField(max_length=30)
    POCHTA_MANZIL = models.TextField()
    BUDGET_0_XUSUSIY_1 = models.CharField(max_length=10)
    MAOSH = models.CharField(max_length=30)
    LAVOZIMGA_QOYILGAN_TALABLAR = models.CharField(max_length=30)
    SOXA = models.TextField()
    XUDUD = models.CharField(max_length=100, default='Жиззах вилояти')
    TUMAN = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.INN

class ArnasoyTumani(BaseTumani):
    TUMAN = 'Арнасой тумани'

class BaxmalTumani(BaseTumani):
    TUMAN = 'Бахмал тумани'

class GallaorolTumani(BaseTumani):
    TUMAN = 'Шароф Рашидов тумани'

class SharofRashidovTumani(BaseTumani):
    TUMAN = 'Шароф Рашидов тумани'

class DostilikTumani(BaseTumani):
    TUMAN = 'Дўстлик тумани'

class ZominTumani(BaseTumani):
    TUMAN = 'Зомин тумани'

class ZarbdorTumani(BaseTumani):
    TUMAN = 'Зарбдор тумани'

class MirzacholTumani(BaseTumani):
    TUMAN = 'Мирзачўл тумани'

class ZafarobodTumani(BaseTumani):
    TUMAN = 'Зафаробод тумани'

class PaxtakorTumani(BaseTumani):
    TUMAN = 'Пахтакор тумани'

class ForishTumani(BaseTumani):
    TUMAN = 'Фориш тумани'

class YangiobodTumani(BaseTumani):
    TUMAN = 'Янгиобод тумани'

class Jizzax(BaseTumani):
    TUMAN = 'Жиззах'
