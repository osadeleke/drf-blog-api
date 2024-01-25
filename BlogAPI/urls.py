from django.urls import path, include
from . import views
from .views import Listblog

urlpatterns = [
    path('bloglist', views.bloglist, name='bloglist'),
    path('allbloglist', Listblog.as_view(), name='allbloglist')
]
