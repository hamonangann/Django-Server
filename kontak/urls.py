from django.urls import path
from kontak.views import kontak, get_kontak_json, add_kontak

urlpatterns = [
    path('', kontak, name='index'),
    path('json/', get_kontak_json, name='get_kontak_json'),
    path('add_kontak/', add_kontak, name='add_kontak')
]