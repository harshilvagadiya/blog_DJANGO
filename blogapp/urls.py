from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('<str:slug>>/', views.blog_detail, name='blog_detail'),
]

