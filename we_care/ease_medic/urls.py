
from django.contrib import admin
from django.urls import path, include
from .views import homePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', homePageView, name='home'),
]
