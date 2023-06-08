from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todoView, name='todoView'),
    path('add/', views.todoAdd, name="todoAdd"),
    path('delete/<int:id>/', views.todoDelete, name="todoDelete"),
]