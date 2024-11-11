from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
]
