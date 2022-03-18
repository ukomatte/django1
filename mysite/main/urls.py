from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('backend', views.backend, name='backend'),
    path('product', views.product, name='product'),
    path('airpods', views.airpods, name='airpods'),
]