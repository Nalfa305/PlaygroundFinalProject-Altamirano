from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

admin.site.site_title = "Products"

class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class CategoryFilter(admin.SimpleListFilter):
    title = _('category')
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return ProductCategory.objects.filter(active=True).values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category_id__id__exact=self.value())
        return queryset

class SubCategoryFilter(admin.SimpleListFilter):
    title = _('subcategory')
    parameter_name = 'subcategory'

    def lookups(self, request, model_admin):
        return ProductSubCategory.objects.filter(active=True).values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subcategory_id__id__exact=self.value())
        return queryset
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "stock", "image", "colour", "update_date"]
    list_display_links = ["name"]
    search_fields = ["name"]
    ordering = ["category_id__name", "name"]
    list_filter = [CategoryFilter, SubCategoryFilter]
    date_hierarchy = "update_date"

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
admin.site.register(Product, ProductAdmin)