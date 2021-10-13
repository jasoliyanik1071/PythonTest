# -*- coding: utf-8 -*-

import logging

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.urls import reverse

from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from user_management.forms import UserRegistrationForm, LoginForm

log = logging.getLogger(__name__)


class RegisterManagement(View):

    #   def __init__(self, *args, **kwargs):
    #     super(RegisterManagement, self).__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        """
            Sets the course id and chapter id
        """
        if request and request.user and request.user.is_authenticated:
            context=dict()
            return render(request, "dashboard.html", context)


    def render_template(self, template_path, context=dict()):
        """
        renders template
        """
        return render(self.request, template_path, context)

    def get(self, request, *args, **kwargs):
        context = {
            "register_form": UserRegistrationForm()
        }
        return self.render_template(template_path="user/register.html", context=context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
                form = UserRegistrationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, "Registration successful." )
                    return redirect("dashboard")

                messages.error(request, "Unsuccessful registration. Invalid information.")

        context = {
            "register_form": UserRegistrationForm()
        }
        return self.render_template(template_path="user/register.html", context=context)


class LoginManagement(View):

    #   def __init__(self, *args, **kwargs):
    #     super(RegisterManagement, self).__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        """
            Sets the course id and chapter id
        """
        if request and request.user and request.user.is_authenticated:
            context=dict()
            return render(request, "dashboard.html", context)


    def render_template(self, template_path, context=dict()):
        """
        renders template
        """
        return render(self.request, template_path, context)

    def get(self, request, *args, **kwargs):
        context = {
            "form": LoginForm()
        }
        return self.render_template(template_path="user/login.html", context=context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, "Registration successful." )
                    return redirect("dashboard")

                messages.error(request, "Unsuccessful registration. Invalid information.")

        context = {
            "form": LoginForm()
        }
        return self.render_template(template_path="user/login.html", context=context)


def dashboard(request):
    context = dict()
    return render(request, "dashboard.html", context)