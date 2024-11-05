from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import UserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Other app URL patterns
    path('api/', include('users.urls')),
]
