from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CreateTask, DeleteTask, Login, Register, TaskList,
                    UpdateTask)

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create/", CreateTask.as_view(), name="create_task"),
    path("update/<int:pk>", UpdateTask.as_view(), name="update_task"),
    path("delete/<int:pk>", DeleteTask.as_view(), name="delete_task"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", Register.as_view(), name="register"),
]
