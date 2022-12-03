from django.urls import path
from .views import index, add_katalog

urlpatterns = [
    path('list_katalog',index,name='list_katalog'),
    path('add_katalog',add_katalog,name='add_katalog')
]