from django.urls import path
from .views import get_all_blogs, get_blog_by_url, post_comment, put_comment, delete_comment

urlpatterns = [
    path('', list_blogs, name='list_blogs'),
    path('add', add_blog, name='add_blog'),
    path('<blog_url>', get_blog_by_url, name='get_blog_by_url'),
    path('delete/<blog_url>', delete_blog, name='delete_blog'),
]

