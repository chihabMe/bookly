from urllib.request import HTTPRedirectHandler
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from helpes.email_generator import email_generator
from .forms import LoginForm, ProfileEditForm,UserCreationForm, UserEditForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponse("logged in ")
        return HttpResponse("invalid login")

    context = {"form": form}
    return render(request, 'accounts/login.html', context)
def logout_view(request):
    logout(request)
    return redirect(reverse("accounts:login"))
     
@login_required
def profile_view(request):

    context = {
        "profile":request.user.profile
    }
    return render(request,"accounts/profile.html",context)
def profile_edit_view(request):
    profile_form = ProfileEditForm(instance=request.user.profile)
    user_form = UserEditForm(instance=request.user)
    if request.method=="POST":
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST  , files=request.FILES  )
        user_form = UserEditForm(instance=request.user,data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect(reverse("accounts:profile"))
    context = {
        "profile_form":profile_form,
        "user_form":user_form
    }
    return render(request,"registration/profile_edit.html",context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            user = form.save()
            return redirect(reverse("accounts:login"))
    context = {
        "form":form,
    }
    return render(request,"registration/register.html",context)

class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self,form):
        messages.success(self.request,"you password has been changed")
        return super().form_valid(form)

