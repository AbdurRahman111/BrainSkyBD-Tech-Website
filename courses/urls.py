from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_page, name='course_page'),
    path('course_details/<str:slug>', views.course_details, name='course_details'),
    path('checkout_form_submit', views.checkout_form_submit, name='checkout_form_submit'),

    path('redirect_to_url', views.redirect_to_url_func, name="redirect_to_url"),
]