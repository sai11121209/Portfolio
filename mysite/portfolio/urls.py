from os import name
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', views.Portfolio, name='home'),
    path('portfolio/<str:username>/<int:pk>/detail', views.ContactDetail, name='detail'),
    path('portfolio/<str:username>/<int:pk>/edit', views.ContactEdit, name='edit'),
]