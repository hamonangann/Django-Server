from django.urls import path
from .views import index, renderJSON, create_promo

urlpatterns = [
    path('',index,name='indexPromo'),
    path('add_promo', create_promo, name="addPromo"),
    path('api_promo', renderJSON, name = "apiPromo")
]