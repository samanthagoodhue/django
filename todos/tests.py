from django.urls import reverse
from rest_framework import status
import pytest

pytestmark = pytest.mark.django_db


def test_todo_list(api_client):
    url = reverse('todo-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_todo_detail(api_client, todo):
    url = reverse('todo-detail', kwargs={'pk': todo.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_todo_create(api_client):
    url = reverse('todo-list')
    data = {'title': 'Test Todo', 'completed': False}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


def test_todo_update(api_client, todo):
    url = reverse('todo-detail', kwargs={'pk': todo.pk})
    data = {'title': 'Updated Todo', 'completed': True}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK


def test_todo_delete(api_client, todo):
    url = reverse('todo-detail', kwargs={'pk': todo.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
