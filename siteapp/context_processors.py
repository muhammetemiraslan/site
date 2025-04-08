from .models import category
from siteConfigurations.models import NavbarItem

def site_info(request):
    return {"copyright_year": 2025, "company_name": "AIKE"}

def categories(request):
    return {
        "categories": category.objects.all()[:5],
    }

def navbar_items(request):
    return {
        'navbar_items': NavbarItem.objects.filter(is_active=True)
    }

def categories(request):
    return {
        "f_categories": category.objects.all()[:5],
    }