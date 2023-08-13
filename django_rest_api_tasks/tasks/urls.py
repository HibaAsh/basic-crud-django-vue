from django.urls import path, include
from .views import TaskViewSet
from rest_framework import routers

taskRouter = routers.DefaultRouter()
taskRouter.register('', TaskViewSet, basename="taskView")
urlpatterns = [
    path("task/", include(taskRouter.urls)),
]