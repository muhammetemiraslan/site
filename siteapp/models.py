from django.db import models


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class product(models.Model):
    title = models.CharField(max_length=250)
    categories = models.ManyToManyField(category, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="siteapp/", blank=True, null=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
