from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/details/<int:todo_id>', views.details), # todo_id === def details(...todo_id)
    path('/add', views.add, name='add')
]
