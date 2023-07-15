import pytest
from django.urls import reverse
from rest_framework import status

from .models import Task


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def task():
    # Create a Task object or retrieve an existing one
    return Task.objects.create(
        title="Example Task", description="testing the task", completed=False
    )


pytestmark = pytest.mark.django_db


def test_task_list(api_client):
    print()
    url = reverse("task-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_task_detail(api_client, task):
    url = reverse("task-detail", kwargs={"pk": task.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    print(response.status_code)


def test_task_create(api_client):
    url = reverse("task-list")
    data = {"title": "Test Task", "description": "testing the task", "completed": False}
    response = api_client.post(url, data)
    print(response.content)
    assert response.status_code == status.HTTP_201_CREATED


def test_task_update(api_client, task):
    url = reverse("task-detail", kwargs={"pk": task.pk})
    data = {
        "title": "Updated Task",
        "description": "testing the task",
        "completed": True,
    }
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK


def test_task_delete(api_client, task):
    url = reverse("task-detail", kwargs={"pk": task.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
