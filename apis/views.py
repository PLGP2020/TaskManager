from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from .serializers import TaskSerializer, TaskHistorySerializer
from .permissions import IsAuthorOrReadOnly

from tasks.models import Task

from datetime import datetime


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    

class DetailTaskView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   
    permission_classes = (permissions.IsAdminUser, )


class AddTaskView(generics.CreateAPIView):
    serializer_class = TaskSerializer  
    permission_classes = [IsAuthenticated]


class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class DeleteTaskView(generics.DestroyAPIView):
    serializer_class = TaskSerializer  
    permission_classes = [IsAuthenticated]    


class FilterTaskView(APIView):
    @login_required
    def get(self, request):

        user_id = request.GET.get("user_id")
        status = request.GET.get("status")
        keyword = request.GET.get("keyword")


        tasks = Task.objects.all()

        if user_id:
            tasks = tasks.filter(user_id=user_id)

        if status:
            tasks = tasks.filter(status=status) 

        if keyword:
            tasks = tasks.filter(name__icontains=keyword) | tasks(description__icontains=keyword)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status=200)


class HistoryTaskView(APIView):
    @login_required
    def get(self, request, pk):

        user_id = request.GET.get("user_id")

        t1 = datetime.now()

        task = Task.objects.get(pk=pk)

        task_history = task.history.all()

        print(task_history)

        serializer = TaskHistorySerializer(task_history, many=True)

        return Response(serializer.data, status=200)
    

        

          
