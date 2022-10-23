from urllib.request import HTTPRedirectHandler
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import LoginForm

# Create your views here.


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
    context = {}
    return render(request,"accounts/profile.html",context)