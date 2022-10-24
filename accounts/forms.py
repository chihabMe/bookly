#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as f
from django.contrib.auth.password_validation import validate_password 
from .models import Profile

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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth","image"]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget=forms.DateInput(attrs={"class":"input is-primary","type":"date"})
        self.fields['image'].widget=forms.FileInput(attrs={"name":"resume","class":"file-input","type":"file"})
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ["first_name","last_name"]


