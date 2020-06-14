from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('mypage/', views.MyPage, name='mypage'),
    path('username_change/<int:pk>', views.UsernameChange, name='username_change'),
]