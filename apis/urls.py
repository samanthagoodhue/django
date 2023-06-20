# apis/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()
router.register("", TaskViewSet, basename="tasks")
urlpatterns = router.urls
