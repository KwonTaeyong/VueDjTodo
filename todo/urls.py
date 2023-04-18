from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoTV, name='index'),
    path('todo/toast/', views.Toast, name='toast'),
]
