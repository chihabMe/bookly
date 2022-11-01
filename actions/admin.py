from django.contrib import admin
from .models import Action

# Register your models here.

@admin.register(Action)
class ActionAdminManger(admin.ModelAdmin):
    list_display= ['profile','body','created','target'] 
