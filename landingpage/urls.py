from django.urls import path
from .views import index, add_konten

urlpatterns = [
    path('',index,name='indexKonten'),
    path('add',add_konten,name='addKonten')
]