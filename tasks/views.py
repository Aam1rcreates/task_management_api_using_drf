
from .models import Task
from .serializers import TaskSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#  For Authentications
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

# class TaskList(APIView):
#         # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                
#         """
#         List all tasks, or create a task.
#         """
#         def get(self, request,):
#             tasks = Task.objects.all()
#             serializer = TaskSerializer(tasks, many=True)
#             return Response(serializer.data)

#         def post(self, request):
#             serializer = TaskSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def perform_create(self, serializer):
#             serializer.save(owner=self.request.user)


class TaskDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    """
    Retrieve, update or delete a task.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'status', 'due_date']
    ordering_fields = ['title','due_date']
    search_fields = ['title', 'description', 'due_date']

    def post(self, request):
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # """
    # List all tasks, or create a task.
    # """
    # def get(self, request,):
    #     tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)    

    


class TaskListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']    


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    