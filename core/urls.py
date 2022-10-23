from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include("accounts.urls", namespace='accounts')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
