from .models import category

def site_info(request):
    return {"copyright_year": 2025, "company_name": "AIKE"}

def categories(request):
    return {
        "f_categories": category.objects.all()[:5],
    }
