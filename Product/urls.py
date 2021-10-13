# -*- coding: utf-8 -*-
"""
    # User-Management URL Configuration
"""

from django.conf.urls import url
from Product.views import ProductManagement, get_onchange_categ_product
# from Product.views import ProductManagement, CategoryManagement


urlpatterns = [
    url(r"product/list$", ProductManagement.as_view(), name="product-list"),
    # url(r"category/list$", CategoryManagement.as_view(), name="category-list"),
    url(r"get-categ-related/product$", get_onchange_categ_product, name="categ-relt-product-list"),
]
