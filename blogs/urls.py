from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<str:slug>',views.blog_details, name = 'blog_details'),
]