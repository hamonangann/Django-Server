from django.urls import path
from .views import index, add_konten, delete_konten, indexAturKonten

urlpatterns = [
    path('',index,name='indexKonten'),
    path('aturKonten/add',add_konten,name='addKonten'),
    path('delete/<int:idKonten>',delete_konten, name='deleteKonten'),
    path('aturKonten',indexAturKonten,name='aturKonten')
]