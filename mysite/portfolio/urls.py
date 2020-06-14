from os import name
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', views.Portfolio, name='home'),
    path('portfolio/<int:pk>/detail', views.ContactDetail, name='detail'),
    path('portfolio/<int:pk>/edit', views.ContactEdit, name='edit'),
]