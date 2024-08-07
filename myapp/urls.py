from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, signup_view

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),  # Use the login_view function
    path('contact/', views.contact, name='contact'),

    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
