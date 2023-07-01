from django.contrib import admin
from django.urls import path
from data_base import views
urlpatterns = [
    path('book_add/', views.book_add),
    path('book_select/', views.book_select),
]