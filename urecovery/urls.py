from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import UserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URL patterns
    path('api/auth/', include([
        path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
        path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
        path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    ])),

    # Other app URL patterns
    path('api/', include('users.urls')),
    path('api/', include('base.urls')),
    path('api/', include('blog.urls')),
]