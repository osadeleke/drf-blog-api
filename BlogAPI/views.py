from django.shortcuts import render
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, mixins, generics

# function based views
# get all blogs
@api_view(['GET', 'POST'])
def bloglist(request):
    all_blogs = Blog.objects.all()
    serializer_blog = BlogSerializer(all_blogs, many=True)
    return Response(serializer_blog.data)

# class based view for list blog
class ListBlog(APIView):
    # get request to retrieve all blogs
    def get(self, request):
        all_blogs = Blog.objects.all()
        serializer_blog = BlogSerializer(all_blogs, many=True)
        return Response(serializer_blog.data)
    
    # post request to add a blog to database
    def post(self, request):
        # use blog serializer to object
        serializer_blog = BlogSerializer(data=request.data)

        # check if object is valid then save object.
        if serializer_blog.is_valid(raise_exception=True):
            blog_saved = serializer_blog.save()
            return Response(f"Success: {blog_saved.title} created successfully...")
        
        # return if object serialized is not valid
        return Response(serializer_blog.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailedBlog(APIView):
    # get blog by id
    def get(self, request, id):
        blog = Blog.objects.filter(id=id)
        serializer_blog = BlogSerializer(blog, many=True)
        return Response(serializer_blog.data)

    # update a blog by id.
    def put(self, request, id):
        blog = Blog.objects.get(id=id)
        serializer_blog = BlogSerializer(blog, request.data)
        
        if serializer_blog.is_valid(raise_exception=True):
            blog_save = serializer_blog.save()
            return Response(f"Success: {blog_save.title} updated successfully...")
        
        return Response(serializer_blog.error, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a blog by id
    def delete(self, request, id):
        blog = Blog.objects.get(id=id)
        title = blog.title
        blog.delete()
        return Response(f"Success: {title} deleted sucessfully...")


# Mixins based views
# get list of blogs
class ListBlogsMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # get works with self.list
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
# handle crud operation for individual blog
class DetailedBlogMixin(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # get here works with self.retrieve
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # post here works with self.create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    #put here works with self.update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # delete here works with self.destroy
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

## Generic views
# get list of blogs
class ListBlogsGeneric(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# crud on single blog
class DetailedBlogGeneric(generics.CreateAPIView,
                          generics.DestroyAPIView,
                          generics.RetrieveAPIView,
                          generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer