
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.blog, name='home'),
    path('blog/post/', views.post, name='post'),
    path('user/', views.User, name='user')
]