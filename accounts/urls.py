#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path,include
from .views import login_view, logout_view, profile_edit_view, profile_view,CustomPasswordChangeView, register_view
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.urls import reverse_lazy
from allauth   import app_settings as allauth_settings

app_name = 'accounts'

urlpatterns = [
    path("login/",LoginView.as_view(),name='login'),
    path("register/",register_view,name='register'),
    path("logout/",logout_view,name='logout'),
    path("profile/",profile_view,name='profile'),
    path("profile/edit/",profile_edit_view,name='profile_edit'),
    ##change password 
    path("password_change/",CustomPasswordChangeView.as_view(success_url=reverse_lazy("accounts:profile")),name='password_change'),
    # path("password_change/done/",PasswordChangeDoneView.as_view(),name='password_change_done'),
    #password reset 
    path("password_reset/",PasswordResetView.as_view(email_template_name='password_reset_email.html',success_url=reverse_lazy("accounts:password_reset_done")),name='password_reset'),
    path("password_reset/done/",PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path("reset/done/",PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

if allauth_settings.SOCIALACCOUNT_ENABLED:
    pass
    # urlpatterns+= [path("social/",include("allauth.socialaccount.urls"))]

