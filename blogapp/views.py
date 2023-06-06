from django.shortcuts import render
from .models import Post
from .forms import commentForms

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()
    new_comments = None
    
    if request.method == 'POST':
        form = commentForms(request.POST)
        if form.is_valid():
            new_comments = form.save(commit=False)
            # print(new_comments)
            new_comments.post = post
            print(new_comments)
            new_comments.save()
            
            
    else:
        form = commentForms()
        
    
    return render(request, 'blog_detail.html', {'post': post, 'form': form, 'comments': comments, 'new_comments': new_comments})
    