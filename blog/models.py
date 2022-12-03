from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=255)
    isi_artikel = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)