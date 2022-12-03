from django.urls import path
from .views import list_blogs, get_blog_by_url, add_blog, delete_blog

urlpatterns = [
    path('', list_blogs, name='list_blogs'),
    path('add', add_blog, name='add_blog'),
    path('<blog_url>', get_blog_by_url, name='get_blog_by_url'),
    path('delete/<blog_url>', delete_blog, name='delete_blog'),
]

