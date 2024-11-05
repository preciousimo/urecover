from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    
    path('users', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('user/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('createuser/', views.UserCreationViewSet.as_view({'post': 'create'}), name='create-user'),
]