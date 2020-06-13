
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.Blog, name='home'),
    path('blog/post/', views.Post, name='post'),
    path('blog/postlist/<int:pk>/', views.PostDetail, name='detail'),
    path('blog/postlist', views.PostList, name='list'),
    path('user/', views.User, name='user'),
]