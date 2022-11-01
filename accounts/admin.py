from django.contrib import admin
from .models import Profile,Contact

# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    fields = ["user","date_of_birth","image"]

@admin.register(Contact)
class AdminProfile(admin.ModelAdmin):
    list_display = ["user_from",'user_to','created']
