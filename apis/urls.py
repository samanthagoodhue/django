from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views

urlpatterns = [
    path('tasks/', views.Tasks.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)