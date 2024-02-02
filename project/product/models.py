from django.db import models
from django.utils import timezone

class ProductCategory(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,verbose_name="descripción")
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

class ProductSubCategory(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,verbose_name="descripción")
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"
    
class Size(models.Model):
    
    name = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)   

class Product(models.Model):
    category_id = models.ManyToManyField(ProductCategory, blank=True, limit_choices_to={'active': True})
    subcategory_id = models.ManyToManyField(ProductSubCategory, blank=True, limit_choices_to={'active': True})
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,verbose_name="descripción")
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='product/static/product/img')
    colour = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name= "update date")
    size = models.ManyToManyField(Size, blank=True, limit_choices_to={'active': True})

    def __str__(self) -> str:
        return f"{self.name} ({self.size}) ${self.price:.2f}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"