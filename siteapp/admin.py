from django.contrib import admin
from .models import category, product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    readonly_fields = ("slug",)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_home", "slug", "get_categories")
    list_filter = ("categories", "price", "is_home")
    search_fields = ("title",)
    readonly_fields = ("slug",)
    inlines = [ProductImageInline]

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    get_categories.short_description = "Categories"




admin.site.register(category, CategoryAdmin)
admin.site.register(product, ProductAdmin)
