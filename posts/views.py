from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # how to get post data of title, content, author
        title = self.request.data.get('title')
        title = "Title of " + title
        serializer.save(title=title)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        # how to get post data of title, content, author
        title = self.request.data.get('title')
        title = "Updated " + title
        serializer.save(title=title)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # how to get post data of title, content, author
        title = self.request.data.get('title')
        title = "Title of " + title
        serializer.save(title=title)

    def perform_update(self, serializer):
        # how to get post data of title, content, author
        title = self.request.data.get('title')
        title = "Updated " + title
        serializer.save(title=title)
