
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.all_blogs , name='blogs'),
    path('<int:blog_id>/' , views.detail, name='detail')    
]
