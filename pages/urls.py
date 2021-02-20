from django.urls import path

from . import views

#Page Content for URL Mapping
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about')
]