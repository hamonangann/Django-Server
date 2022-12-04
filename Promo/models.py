from django.db import models

# Create your models here.
class Promo(models.Model) :
    idPromo = models.BigAutoField(primary_key=True)
    namaPromo = models.CharField(max_length=30)
    gambarPromo = models.CharField(max_length=500)
    detailsPromo = models.TextField()
    tanggalExp = models.DateField()