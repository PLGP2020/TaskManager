from django.urls import path

from .views import TaskListView, DetailTaskView, AddTaskView, UpdateTaskView, DeleteTaskView, FilterTaskView, HistoryTaskView

urlpatterns = [
     path('', TaskListView.as_view(), name='task_list'),
     path('<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
     path('new_task/', AddTaskView.as_view(), name='add_task'),
     path('update/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
     path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
     path('filter/', FilterTaskView.as_view(), name='filter_tasks'),
     path('history/<int:pk>', HistoryTaskView.as_view(), name='task_history'),
]