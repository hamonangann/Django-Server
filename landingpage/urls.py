from django.urls import path
from .views import index, add_konten, delete_konten, indexAturKonten, detail_konten

urlpatterns = [
    path('',index,name='indexKonten'),
    path('aturKonten/add',add_konten,name='addKonten'),
    path('delete/<int:idKonten>',delete_konten, name='deleteKonten'),
    path('aturKonten',indexAturKonten,name='aturKonten'),
    path('konten/<int:idKonten>', detail_konten, name='detailKonten')
]