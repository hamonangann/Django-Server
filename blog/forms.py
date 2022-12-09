from django import forms
from blog.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['judul', 'isi_artikel', 'url_gambar']
