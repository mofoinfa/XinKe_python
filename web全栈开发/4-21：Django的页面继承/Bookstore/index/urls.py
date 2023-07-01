from django.contrib import admin
from django.urls import path
from index import views

# 子路由
urlpatterns = [
    path('father/', views.father_html),
    path('sun/', views.sun_html, name='num'),
]
