#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import login_view, logout_view, profile_view,CustomPasswordChangeView
from django.contrib.auth.views import LoginView,PasswordChangeDoneView,PasswordChangeView
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    #path("login/", login_view, name='login'),
    path("login/",LoginView.as_view(),name='login'),
    path("logout/",logout_view,name='logout'),
    path("profile/",profile_view,name='profile'),
    ##change password 
    path("password_change/",CustomPasswordChangeView.as_view(success_url=reverse_lazy("accounts:profile")),name='password_change'),
    # path("password_change/done/",PasswordChangeDoneView.as_view(),name='password_change_done'),
]
