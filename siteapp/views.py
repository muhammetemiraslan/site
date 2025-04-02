from django.shortcuts import render
from .models import product, category

# Create your views here.

def home(request):
    products = product.objects.all()[:3]
    
    categories = category.objects.all()

    return render(request, "siteapp/index.html",
    {
        "products":products,
        "categories":categories,
    })

def Category(request):
    return render(request, "siteapp/category.html")


def promo(request):
    return render(request, "siteapp/promo.html")

def interiorDesign(request):
    return render(request, "siteapp/interior-design.html")

def products(request):

    products = product.objects.all()
    
    categories = category.objects.all()

    return render(request, "siteapp/products.html", 
    {
        "products":products,
        "categories":categories,
    })