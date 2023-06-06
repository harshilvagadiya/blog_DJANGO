from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to= 'img', height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    commenter = models.CharField(max_length=500)
    body = models.TextField(max_length=510)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.body