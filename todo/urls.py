from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.task_list, name='tasks'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]

