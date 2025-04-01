from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "siteapp/index.html")

def category(request):
    return render(request, "siteapp/category.html")


def promo(request):
    return render(request, "siteapp/promo.html")

def interiorDesign(request):
    return render(request, "siteapp/interior-design.html")

def productRecomendation(request):
    return render(request, "siteapp/product-recomendation.html")