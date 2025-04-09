# your_app/admin.py
from django.contrib import admin
from django import forms
from .models import NavbarItem
from .utils import get_named_urls

class NavbarItemForm(forms.ModelForm):
    url_name = forms.ChoiceField(choices=[], required=True)

    class Meta:
        model = NavbarItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url_name'].choices = get_named_urls()

class NavbarItemAdmin(admin.ModelAdmin):
    form = NavbarItemForm
    list_display = ('name', 'url_name', 'is_active', 'position')
    list_editable = ('position',)
    ordering = ['position']

admin.site.register(NavbarItem, NavbarItemAdmin)
