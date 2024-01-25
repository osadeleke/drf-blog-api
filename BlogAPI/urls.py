from django.urls import path, include
from . import views

urlpatterns = [
    path('bloglist', views.bloglist, name='bloglist'),
]
