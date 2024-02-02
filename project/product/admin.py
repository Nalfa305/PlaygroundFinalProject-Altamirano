from django.contrib import admin
from .models import *

admin.site.site_title = "Products"

class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "stock", "image", "colour", "update_date"]
    list_display_links = ["name"]
    search_fields = ["name"]
    ordering = ["category_id", "subcategory_id", "name"]
    list_filter = ["category_id", "subcategory_id"]
    date_hierarchy = "update_date"

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
admin.site.register(Product, ProductAdmin)