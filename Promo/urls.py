from django.urls import path
from .views import index, add_promo

urlpatterns = [
    path('',index,name='indexPromo'),
    path('add_promo',add_promo,name='addPromo')
]