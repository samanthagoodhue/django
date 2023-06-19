# apis/serializers.py
from rest_framework import serializers

from tasks import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Task
