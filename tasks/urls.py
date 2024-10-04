from django.urls import path
from .views import tasks, create_task, detail, update, completed, deleted, deletetask

urlpatterns = [
    path('tasks/', tasks, name='tasks'),
    path('createtask/',create_task, name='create_task'),
    path('detailtask/<int:taskid>/', detail, name='detail'),
    path('updatetask/<int:taskid>/', update, name='update'),
    path('completedtask/<int:taskid>/', completed, name='completed'),
    path('deletedtask/<int:taskid>/', deleted, name='deleted'),
    path('deletetask/<int:taskid>/', deletetask, name='deletetask'),
]