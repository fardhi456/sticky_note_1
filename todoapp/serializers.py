from rest_framework import serializers
from .models import TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'


def get_queryset(self):
    return TodoTask.objects.filter(user=self.request.user)

def perform_create(self, serializer):
    serializer.save(user=self.request.user)
