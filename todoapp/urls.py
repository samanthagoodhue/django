from django.urls import include, path
from tasks import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls"))
]
