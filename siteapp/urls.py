from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('category/', views.Category, name="Category"),
    path('promo/', views.promo, name="promo"),
    path('interior-design/', views.interiorDesign, name="interior-design"),
    path('products/', views.products, name="products"),   
    path('products/<slug:slug>', views.product_details, name="product-details"),
    path('products/category/<slug:slug>/', views.products_by_category, name="products-by-category"),
]