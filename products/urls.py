from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/<str:slug>', views.product_details, name='product_details'),
]