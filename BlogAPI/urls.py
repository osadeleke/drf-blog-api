from django.urls import path, include
from . import views
from .views import ListBlog, DetailedBlog, ListBlogsMixin, DetailedBlogMixin, ListBlogsGeneric, DetailedBlogGeneric

urlpatterns = [
    path('bloglist', views.bloglist, name='bloglist'),
    path('allbloglist', ListBlog.as_view(), name='allbloglist', ),
    path('blog/<int:id>', DetailedBlog.as_view(), name='detailedblog'),
    # mixinx views
    path('mixinallblogs', ListBlogsMixin.as_view(), name='mbv'),
    path('mixinblog/<int:pk>', DetailedBlogMixin.as_view(), name='dbv'),
    # generic views
    path('genericlist', ListBlogsGeneric.as_view(), name='lbg'),
    path('genericdetail/<int:pk>', DetailedBlogGeneric.as_view(), name='dbg'),
]
