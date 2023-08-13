from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']

    # def update(self, instance, validated_data):
    #     print("validated data:", validated_data)
    #     instance.title = validated_data["title"]
    #     instance.description = validated_data["description"]
    #     instance.completed = validated_data["completed"]
    #     instance.save()

    #     return instance