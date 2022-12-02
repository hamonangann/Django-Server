from django.urls import path
from .views import index, add_konten, delete_konten

urlpatterns = [
    path('',index,name='indexKonten'),
    path('add',add_konten,name='addKonten'),
    path('delete/<int:idKonten>',delete_konten, name='deleteKonten')
]