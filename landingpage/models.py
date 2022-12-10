from django.db import models

class Konten(models.Model):
    idKonten = models.BigAutoField(primary_key=True)
    judulKonten = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=500)
    isiKonten = models.TextField()

    class Meta:
        ordering = ['-idKonten']


