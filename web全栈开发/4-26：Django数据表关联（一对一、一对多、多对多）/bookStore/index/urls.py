from django.contrib import admin
from django.urls import path
from index import views

# 子路由
urlpatterns = [
    # path('book_add/', views.book_add),
    path('book_select/', views.book_select),
]
