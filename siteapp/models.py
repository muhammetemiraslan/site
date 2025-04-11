from django.db import models
from django.utils.text import slugify
import tinify
from django.conf import settings

# Create your models here.


# 127.0.0.1:8000/category/{category-name}
class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        null=False, unique=True, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class product(models.Model):
    title = models.CharField(max_length=250)
    categories = models.ManyToManyField(category, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="siteapp/", blank=True, null=True)
    description = models.CharField(max_length=255)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(
        null=False, blank=True, unique=True, db_index=True, editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, editable=False
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        if self.image:
            self.compress_image()

    def compress_image(self):
        if self.image:
            image_path = self.image.path
            source = tinify.from_file(image_path)
            source.to_file(image_path)


class ProductImage(models.Model):
    product = models.ForeignKey(
        "product", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.compress_image()

    def compress_image(self):
        if self.image:
            image_path = self.image.path
            source = tinify.from_file(image_path)
            source.to_file(image_path)
