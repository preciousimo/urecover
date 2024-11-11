from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'image', 'category', 'tags', 'published_date', 'status', 'created_at']
