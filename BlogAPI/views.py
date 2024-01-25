from django.shortcuts import render
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# get all blogs
@api_view(['GET', 'POST'])
def bloglist(request):
    all_blogs = Blog.objects.all()
    serializer_blog = BlogSerializer(all_blogs, many=True)
    return Response(serializer_blog.data)