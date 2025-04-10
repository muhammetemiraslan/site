from .models import category
from siteConfigurations.models import NavbarItem
from django.http import HttpRequest

def site_info(request):
    return {"copyright_year": 2025, "company_name": "AIKE"}

def categories(request):
    return {
        "f_categories": category.objects.all()[:5],
    }

def navbar_items(request):
    return {
        'navbar_items': NavbarItem.objects.filter(is_active=True)
    }

def cart_item_count(request: HttpRequest):
    # Sepet verisini session'dan al
    cart = request.session.get("cart", {})

    # Sepetteki toplam ürün sayısını hesapla
    total_items = sum(cart.values())

    return {
        'total_items': total_items
    }
