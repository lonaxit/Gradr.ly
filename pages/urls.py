from django.urls import path

from . import views


app_name = 'pages'

#Page Content for URL Mapping
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name ='services'),
    path('portfolio/', views.products, name = 'products'),
    path('contact/', views.contactus, name = 'contactus'),
]