from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog_detail.html', {'blog_detail': blog_detail})
    