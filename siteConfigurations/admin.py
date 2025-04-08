from django.contrib import admin
from .models import NavbarItem

@admin.register(NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_name', 'is_active')
    list_editable = ('is_active',)