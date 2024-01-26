from django.urls import path
from .views import Blogs, DetailedBlog, Comments, DetailedComment



urlpatterns = [
    path('blogs', Blogs.as_view(), name='bloglist'),
    path('<int:blog_id>', DetailedBlog.as_view(), name='detailedblog'),
    path('<int:blog_id>/comments', Comments.as_view(), name='comment'),
    path('comment/<int:comment_id>', DetailedComment.as_view(), name='comment'),
]
