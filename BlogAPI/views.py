from django.shortcuts import render
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# get all blogs
@api_view(['GET', 'POST'])
def bloglist(request):
    all_blogs = Blog.objects.all()
    serializer_blog = BlogSerializer(all_blogs, many=True)
    return Response(serializer_blog.data)

# class view for list blog
class Listblog(APIView):
    # get request to retrieve all blogs
    def get(self, request):
        all_blogs = Blog.objects.all()
        serializer_blog = BlogSerializer(all_blogs, many=True)
        return Response(serializer_blog.data)
    
    # post request to add a blog to database
    def post(self, request):
        serializer_blog = BlogSerializer(data=request.data)

        if serializer_blog.is_valid(raise_exception=True):
            blog_saved = serializer_blog.save()
            return Response(f"Success: {blog_saved.title} created successfully...")
        return Response(serializer_blog.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class Detailedblog(APIView):
#     def get(self, response):

