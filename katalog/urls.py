from django.urls import path
from .views import index, add_katalog, detail_katalog

urlpatterns = [
    path('',index,name='list_katalog'),
    path('add_katalog',add_katalog,name='add_katalog'),
    path('<int:idKatalog>', detail_katalog, name='detail_katalog'),
]