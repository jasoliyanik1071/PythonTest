# -*- coding: utf-8 -*-

import datetime
import logging
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

from django.core.exceptions import ValidationError


log = logging.getLogger(__name__)


_PASSWORD_INVALID_MSG = _("A valid password is required")


class UserRegistrationForm(UserCreationForm):
    
    """
        - Used to create User Registration form
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean(self):
        """
            # Override the clean method and change the behaviour with user condition basis
            - Check if email is exist or not?

        """
        error_message = False
        email = self.cleaned_data.get('email', False)
        existing = User.objects.filter(email__iexact=email) if email else email
        if existing:
            error_message = "Email ID is already registered. Please use another Email ID to complete Registration."

        if error_message:
            raise forms.ValidationError(_(error_message))

        return self.cleaned_data


class LoginForm(forms.Form):
    """
        - 
    """

    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Email ID *"})
    )
    password = forms.CharField(
        min_length=2,
        required=True,
        error_messages={
            "required": _PASSWORD_INVALID_MSG,
            "min_length": _PASSWORD_INVALID_MSG,
        },
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password *"})
    )

    def clean_email(self):
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists() and existing[0].is_active:
            return self.cleaned_data['email']
        elif existing.exists() and not existing[0].is_active:
            raise forms.ValidationError(_("Your account has not been activated. Please contact Administrator to Activate your Account."))
        else:
            raise forms.ValidationError(_("User Does not exists with this email."))
