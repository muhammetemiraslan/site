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

    valid_filters = ['popular', 'azalan', 'artan', 'yeni']
    filter_option = request.GET.get('filter', 'popular')
    
    if filter_option not in valid_filters:
        filter_option = 'popular'

    if filter_option == 'popular':
        products = product.objects.all()
    elif filter_option == 'azalan':
        products = product.objects.all().order_by('-price')
    elif filter_option == 'artan':
        products = product.objects.all().order_by('price')
    elif filter_option == 'yeni':
        products = product.objects.all().order_by('-created_at')
    else:
        products = product.objects.all()

    return render(request, "siteapp/products.html", 
    {
        "products":products,
        "categories":categories,
    })

def product_details(request, slug):
    products = product.objects.get(slug=slug)

    return render(request,"siteapp/product-details.html",
    {
        "products":products
    })

def products_by_category(request, slug):

    category_slug = slug
    category_obj = category.objects.get(slug=slug)
    products = product.objects.filter(categories=category_obj)
    categories = category.objects.all()

    return render(request, "siteapp/products.html", {
        "products": products,
        "categories": categories,
        "selected_category": category_obj,
        "category_slug": category_slug
    })