#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as f
from django.contrib.auth.password_validation import validate_password 

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(validators=[validate_password],widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email"]
    
    def clean_re_password(self):
        cd = self.cleaned_data 
        if cd.get("password") != cd.get("re_password"):
            self.add_error(field="password",error="Password don't match")
            raise forms.ValidationError("Passwords don't match")
        return cd["re_password"]
    def save(self,commit=True,*args, **kwargs):
        cd = self.cleaned_data
        username = cd['username']
        email = cd['email']
        password = cd['password']
        user = User(username=username,email=email)
        user.set_password(password)
        if commit:
            user.save()
        return user

    


