from django.contrib import admin
from django.urls import path
from index import views

# 子路由
urlpatterns = [
    path('test1/', views.test_html),
    path('test1/<int:id>', views.test_html, name='num'),
    path('defined/',views.defined)
]
