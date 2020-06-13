from os import name
from django.urls import path,include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', views.Portfolio, name='home'),
    path('portfolio/<int:pk>', views.ContactDetail, name='detail'),
]