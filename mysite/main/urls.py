from django.urls import path
from main import views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('backend', views.backend, name='backend'),
    path('product', views.product, name='product'),
    path('airpods', views.airpods, name='airpods'),
    path('iphone', views.iphone, name='iphone'),
]