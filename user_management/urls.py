# -*- coding: utf-8 -*-
"""
    # User-Management URL Configuration
"""

from django.conf.urls import url
from user_management.views import RegisterManagement, LoginManagement


urlpatterns = [
    url(r"user/registration$", RegisterManagement.as_view(), name="register"),
    url(r"user/login$", LoginManagement.as_view(), name="login"),
]
