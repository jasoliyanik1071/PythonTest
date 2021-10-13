# -*- coding: utf-8 -*-

from django.contrib import admin

from Product.models import ProductCategory, ProductProduct


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "sub_category"]
    search_fields = ["name"]
    list_filter = ["name",]
    readonly_fields = ["created", "modified"]
    list_per_page = 10


class ProductProductAdmin(admin.ModelAdmin):

    list_display = ["name", "product_code", "product_price", "product_category", "manufacture_date", "expiry_date", "product_status"]
    search_fields = ["name", "product_code", "product_price", "product_category", "manufacture_date", "expiry_date", "product_status"]
    list_filter = ["name", "product_code", "product_category__name", "product_status"]
    # readonly_fields = ["created", "modified", "created_by"]
    readonly_fields = ["created", "modified"]
    list_per_page = 10


    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.modified_by = user
        instance.save()
        return instance


admin.site.register(ProductCategory, ProductCategoryAdmin)    
admin.site.register(ProductProduct, ProductProductAdmin)    