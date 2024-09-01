from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        status_value = request.data.get('status')

        if not title:
            return Response({'error': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if status_value not in ['pending', 'completed']:
            return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, id, *args, **kwargs):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        todo = self.get_object(id)
        title = request.data.get('title')
        description = request.data.get('description')
        status_value = request.data.get('status')

        if title is not None and not title:
            return Response({'error': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if status_value is not None and status_value not in ['pending', 'completed']:
            return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        todo = self.get_object(id)
        todo.delete()
        return Response({'message': 'Todo item successfully deleted.'}, status=status.HTTP_200_OK)
