from django.contrib import admin
from django.urls import path
from todos.views import TodoListCreateAPIView, TodoDetailAPIView

urlpatterns = [
    path('apis/', TodoListCreateAPIView.as_view(), name='todo-list'),
    path('apis/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
    path('admin/', admin.site.urls)
]