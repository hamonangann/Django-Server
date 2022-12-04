from django.db import models

# Create your models here.
class Kontak(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)
    no_telpon = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    link = models.CharField(max_length=255)





