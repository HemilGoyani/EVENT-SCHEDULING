from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=204)
