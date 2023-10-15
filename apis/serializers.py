from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'user')

class TaskHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Task.history.model 
        fields = '__all__'