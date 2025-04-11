from django.shortcuts import render
from .models import product, category


def home(request):
    products = product.objects.filter(is_home=True)[:4]
    categories = category.objects.all()[:8]

    return render(
        request,
        "siteapp/index.html",
        {
            "products": products,
            "categories": categories,
        },
    )

def Category(request):
    return render(request, "siteapp/category.html")

def promo(request):
    return render(request, "siteapp/promo.html")

def about(request):
    return render(request, "siteapp/about.html")

def products(request):

    products = product.objects.all()
    products_list = product.objects.all()

    categories = category.objects.all()[:8]

    valid_filters = {"azalan": "-price", "artan": "price", "yeni": "-created_at"}

    filter_option = request.GET.get("filter", "test")

    if filter_option in valid_filters:
        products = products.order_by(valid_filters[filter_option])

    return render(
        request,
        "siteapp/products.html",
        {
            "products": products,
            "categories": categories,
            "selected_filter": filter_option,
        },
    )

def product_details(request, slug):
    products = product.objects.get(slug=slug)
    categories = products.categories.all()
    related_products = product.objects.filter(categories__in=categories).exclude(
        id=products.id
    )

    product_images = products.images.all()

    cart = request.session.get('cart', {})  
    cart_quantity = cart.get(str(products.id), 0)

    return render(
        request,
        "siteapp/product-details.html",
        {
            "products": products,
            "categories": categories,
            "related_products": related_products,
            "cart_quantity": cart_quantity,
            "product_images": product_images,
        },
    )

def products_by_category(request, slug):

    category_slug = slug
    category_obj = category.objects.get(slug=slug)
    products = product.objects.filter(categories=category_obj)
    categories = category.objects.all()[:8]

    valid_filters = {"azalan": "-price", "artan": "price", "yeni": "-created_at"}

    filter_option = request.GET.get("filter", "test")

    if filter_option in valid_filters:
        products = products.order_by(valid_filters[filter_option])

    return render(
        request,
        "siteapp/products.html",
        {
            "products": products,
            "categories": categories,
            "selected_category": category_obj,
            "category_slug": category_slug,
            "category_slug": category_slug,
            "selected_filter": filter_option,
        },
    )


# def categoryFooter(request):

    categories = category.objects.all()[:5]

    return render(
        request,
        "_footer.html",
        {
            "categories": categories,
        },
    )