from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/', views.category, name="category"),
    path('promo/', views.promo, name="promo"),
    path('interior-design/', views.interiorDesign, name="interior-design"),
    path('product-recomendation/', views.productRecomendation, name="product-recomendation"),

    
]
