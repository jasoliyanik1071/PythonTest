# -*- coding: utf-8 -*-

import logging

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.urls import reverse

from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from django.http import JsonResponse, HttpResponse

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from Product.models import ProductCategory, ProductProduct


log = logging.getLogger(__name__)


class ProductManagement(View):

    def render_template(self, template_path, context=dict()):
        """
        renders template
        """
        return render(self.request, template_path, context)

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request, *args, **kwargs):
        context = dict()
        context.update({
            "all_category": ProductCategory.objects.defer(),
            "all_product": ProductProduct.objects.defer()
        })
        return self.render_template(template_path="product/product-details.html", context=context)



def get_onchange_categ_product(request):
    context = dict()

    try:
        if "category_id" in request.POST:

            category_id = request.POST.get("category_id")
            if category_id:
                context.update({
                    "all_product": ProductProduct.objects.defer().filter(product_category__id=category_id)
                })
                product_list_data = render_to_string("product/product-data.html", context=context)
                return JsonResponse({
                    'status': 'success',
                    "product_list_data": product_list_data,
                })

        context.update({
            "all_product": ProductProduct.objects.defer()
        })
        product_list_data = render_to_string("product/product-data.html", context=context)
        return JsonResponse({
            'status': 'success',
            "product_list_data": product_list_data,
        })
        
    except Exception as e:
        import traceback
        log.exception(traceback.print_exc())
        return JsonResponse({'status': 'error', 'message': str(e)})
