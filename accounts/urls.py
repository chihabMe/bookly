#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import login_view, logout_view, profile_view
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'accounts'
urlpatterns = [
    #path("login/", login_view, name='login'),
    path("login/",LoginView.as_view(),name='login'),
    path("logout/",logout_view,name='logout'),
    path("profile/",profile_view,name='profile'),
]
