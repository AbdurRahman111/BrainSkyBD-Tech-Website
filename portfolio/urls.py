from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('search_product',views.search_product, name = 'search_product'),
    path('service_AI_and_Machine_Learning',views.service_AI_and_Machine_Learning, name = 'service_AI_and_Machine_Learning'),
    path('service_Mobile_App_Development',views.service_Mobile_App_Development, name = 'service_Mobile_App_Development'),
    path('service_Web_Development',views.service_Web_Development, name = 'service_Web_Development'),
    path('service_Creative_and_Marketing',views.service_Creative_and_Marketing, name = 'service_Creative_and_Marketing'),
    path('portfolio/',views.portfolio, name = 'portfolio'),
    path('Newsletter_submit/',views.Newsletter_submit, name = 'Newsletter_submit'),
    path('contact/', views.contact, name= 'contact'),
    path('services/', views.services, name= 'services'),
    path('demo_request/', views.demo_request, name= 'demo_request'),
    path('Terms_of_use/', views.Terms_of_use, name= 'Terms_of_use'),
    path('Terms_and_conditions/', views.Terms_and_conditions, name= 'Terms_and_conditions'),
    path('Privacy_policy/', views.Privacy_policy, name= 'Privacy_policy'),
    path('Cookie_policy/', views.Cookie_policy, name= 'Cookie_policy'),
    path('about_us/', views.about_us, name= 'about_us'),
]