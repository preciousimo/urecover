from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from blog.models import Blog
from blog.serializers import BlogSerializer

class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogListView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
