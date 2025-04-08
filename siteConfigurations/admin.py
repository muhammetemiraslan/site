from django.contrib import admin
from .models import NavbarItem

class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_name', 'is_active', 'position')
    list_editable = ('position',)
    ordering = ['position']

admin.site.register(NavbarItem, NavbarItemAdmin)