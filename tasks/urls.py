from django.urls import path
from . import views
from .api_views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, RegisterAPIView, mark_task_complete
app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='api-task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='api-task-detail'),
    path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('api/tasks/<int:pk>/mark_complete/', mark_task_complete, name='api-task-mark-complete'),
] 