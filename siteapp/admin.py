from django.contrib import admin
from .models import category, product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    list_filter = ("categories",)
    search_fields = ("title",)

admin.site.register(category, CategoryAdmin)
admin.site.register(product, ProductAdmin)