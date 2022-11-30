from django.urls import path
from authpage.views import login_request, logout_request

urlpatterns = [
    path("lambda", login_request, name="lambda"),
    path("omega", logout_request, name="omega")
]
