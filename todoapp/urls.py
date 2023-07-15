from django.contrib import admin
from django.urls import path

from tasks.views import TaskDetailAPIView, TaskListCreateAPIView

urlpatterns = [
    path("apis/", TaskListCreateAPIView.as_view(), name="task-list"),
    path("apis/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
    path("admin/", admin.site.urls),
]
