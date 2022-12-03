from django.db import models


# Create your models here.
class Katalog(models.Model):
    idKatalog = models.BigAutoField(primary_key=True)
    judulKatalog = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=500)
    deskripsiKatalog = models.TextField()
    hargaKatalog = models.CharField(max_length=30)


