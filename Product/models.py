# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

PRODUCT_STATUS = (
    ("raw_material", "Raw Material"),
    ("in_progress", "In-Progress"),
    ("completed", "Completed"),
)


class ProductCategory(TimeStampedModel):

    name = models.CharField(_("Category Name"), max_length=1024, help_text=_("Name of the category | Used to define product category"))
    sub_category = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class ProductProduct(TimeStampedModel):

    name = models.CharField(_("Product Name"), max_length=1024, help_text=_("Used to store name of the Product"))
    product_code = models.CharField(_("Product Code"), max_length=1024, help_text=_("Used to store Product Code"), null=True, blank=True)
    product_price = models.FloatField(_("Product Price"), default=0.0, help_text=_("Used to store Product Price"))
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True, null=True)
    manufacture_date = models.DateField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(max_length=100, blank=True, null=True)
    product_status = models.CharField(choices=PRODUCT_STATUS, max_length=100)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name
