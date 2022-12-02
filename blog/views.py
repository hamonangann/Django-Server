from django.shortcuts import render
from .models import Blog

# Create your views here.
def list_blog(request):
    blogs = Blog.objects.all().values()
    return render(request, 'blogs.html', {'blogs': blogs})

def get_blog_by_url(request, blog_url):
    blog = Blog.objects.get(pk=blog_url)
    return render(request, 'blog_detail.html', response)

@login_required(login_url='/hello')
def add_blog(request):
    form = BlogForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/blog')
    
    # GET Request
    return render(request, 'blog_form.html', {'form': form})

@login_required(login_url='/hello')
def delete_blog(request, blog_url):
    blog = Blog.objects.get(pk=blog_url)
    blog.delete()
    messages.success(request, 'Your comment is successfully deleted :)')
    return redirect('/blog')
