from re import template
from urllib.request import HTTPRedirectHandler
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from accounts.models import Contact, Profile
from actions.utils import create_action
from common.decorators import hx_required
from common.http_helpers import is_hx_request

# from helpes.email_generator import email_generator
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

def profiles_list_page(request):
    template_name = 'profile/list.html'
    profiles = Profile.objects.all()
    context = {
        "profiles":profiles
    }
    return render(request,template_name,context)

@login_required
@hx_required
def profile_follow(request,username):
    profile = get_object_or_404(Profile , user__username=username)
    template_name = 'profile/partials/un_follow_btn.html'
    if  profile in request.user.profile.following.all():
        # request.user.profile.following.remove(profile)
        Contact.objects.filter(user_from=request.user.profile,user_to=profile).delete()
        create_action(request.user.profile,f'you started following {profile.user.username}',profile)
        template_name='profile/partials/follow_btn.html'
    else:
        create_action(request.user.profile,f'you are not  following {profile.user.username} anymore',profile)
        Contact.objects.create(user_from=request.user.profile,user_to=profile)
    return render(request,template_name,{})

@login_required
def profile_view(request,username=None):
    template_name = 'profile/detail.html'
    if username:
        profile = get_object_or_404(Profile,user__username=username)
    else :
        profile = request.user.profile
    context = {
        "profile":profile
    }
    return render(request,template_name,context)


@login_required
def profile_edit_view(request):
    template_name = "profile/edit.html"
    profile_form = ProfileEditForm(instance=request.user.profile)
    user_form = UserEditForm(instance=request.user)
    if request.method=="POST":
        
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST  , files=request.FILES  )
        user_form = UserEditForm(instance=request.user,data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request,"your profile has been updated successfully")
            return redirect(reverse("accounts:profile"))
    context = {
        "profile_form":profile_form,
        "user_form":user_form
    }
    return render(request,template_name,context)



