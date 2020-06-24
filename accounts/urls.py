from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('mypage', views.MyPage, name='mypage'),
    path('information_change/<str:username>', views.UserInformationChange, name='information_change'),
]