from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer

