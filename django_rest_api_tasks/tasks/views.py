from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    