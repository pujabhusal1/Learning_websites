from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),  # Add this line for contact page
]
