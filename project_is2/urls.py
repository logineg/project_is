"""Файл служит для того, чтобы определить схемы URL для project_is2"""
from django.urls import path
from . import views

app_name = 'project_is2'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    #Все страницы с подробной информацией по определенной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
