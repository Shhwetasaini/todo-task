from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:id>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-retrieve-update-destroy'),
]
