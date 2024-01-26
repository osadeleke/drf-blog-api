from django.shortcuts import render
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class Blogs(APIView):
    def get(self, request):
        try:
            blog = Blog.objects.all()
            serializer = BlogSerializer(blog, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})
        
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Blog Created Successfully'})
        else:
            return Response(serializer.errors)

class DetailedBlog(APIView):
    def get(self, request, blog_id):
        try:
            blog_n = Blog.objects.get(id=blog_id)
            serializer = BlogSerializer(blog_n)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})
        
    def put(self, request, blog_id):
        try:
            blog_n = Blog.objects.get(id=blog_id)
            serializer = BlogSerializer(blog_n, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Blog Updated Successfully'})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({'error': str(e)})

    def delete(self, request, blog_id):
        try:
            blog_n = Blog.objects.get(id=blog_id)
            blog_n.delete()
            return Response({'message': 'Blog Deleted Successfully'})
        except Exception as e:
            return Response({'error': str(e)})
        

class Comments(APIView):
    def get(self, request, blog_id):
        try:
            comment = Comment.objects.filter(blog=blog_id)
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})
        
    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(blog=blog)
                return Response({'message': 'Comment Created Successfully'})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({'error': str(e)})
        
    
class DetailedComment(APIView):
    def get(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})

    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Comment Updated Successfully'})
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({'error': str(e)})
        
    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response({'message': 'Comment Deleted Successfully'})
        except Exception as e:
            return Response({'error': str(e)})