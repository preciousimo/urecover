from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import redirect_to_swagger
from users.views import UserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="U-Recover API",
      default_version='v1',
      description="Backend API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="preciousimoniakemu@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', redirect_to_swagger),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

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