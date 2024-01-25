from django.urls import path, include
from . import views
from .views import ListBlog, DetailedBlog, ListBlogsMixin, DetailedBlogMixin

urlpatterns = [
    path('bloglist', views.bloglist, name='bloglist'),
    path('allbloglist', ListBlog.as_view(), name='allbloglist', ),
    path('blog/<int:id>', DetailedBlog.as_view(), name='detailedblog'),
    # mixinx views
    path('mixinallblogs', ListBlogsMixin.as_view(), name='mbv'),
    path('mixinblog/<int:pk>', DetailedBlogMixin.as_view(), name='dbv'),
]
