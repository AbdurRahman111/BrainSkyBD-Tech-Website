from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_product_page, name='digital_product_page'),
    path('digital_product_details/<str:slug>', views.digital_product_details, name='digital_product_details'),
    path('digital_product_checkout_form_submit', views.digital_product_checkout_form_submit, name='digital_product_checkout_form_submit'),
    path('proDentim-product', views.proDentim_product, name='proDentim_product'),
]