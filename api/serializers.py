from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Project, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['done'] = instance.is_done()
        ret['status'] = instance.Status(instance.status).label
        return ret

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'task_set']
        depth = 1

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['done'] = instance.is_done()
        return ret

