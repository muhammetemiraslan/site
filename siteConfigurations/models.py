from django.db import models
from django.urls import reverse_lazy

class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            return reverse_lazy(self.url_name)
        except:
            return '#'
