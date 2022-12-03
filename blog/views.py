from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def list_blogs(request):
    blogs = Blog.objects.all().values()
    return render(request, 'blogs.html', {'blogs': blogs})

def get_blog_by_url(request, blog_url):
    blog = Blog.objects.get(pk=blog_url)
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required(login_url='/hello')
def add_blog(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    
    # GET Request
    return render(request, 'blog_form.html', {'form': form})

@login_required(login_url='/hello')
def delete_blog(request, blog_url):
    blog = Blog.objects.get(pk=blog_url)
    blog.delete()
    messages.success(request, 'Your comment is successfully deleted :)')
    return HttpResponseRedirect('/blog')
