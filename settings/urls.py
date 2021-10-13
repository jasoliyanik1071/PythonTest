# -*- coding: utf-8 -*-

"""
	# ProductManagement URL Configuration
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from user_management import views as user_views

# LMS URLs starts here
urlpatterns = [
    # Default admin URL's
    url(r'^admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')), # new


    url(r'^dashboard$', user_views.dashboard, name="dashboard"),
    url(r'^$', user_views.dashboard, name="dashboard"),

    # Custom URL's
    url(r'^', include(("user_management.urls", "user_management"), namespace="user_management")),
    url(r'^', include(("Product.urls", "product_management"), namespace="product_management")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
