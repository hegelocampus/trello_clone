from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import ProjectSerializer, TaskSerializer, UserSerializer
from .models import Project, Task

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

