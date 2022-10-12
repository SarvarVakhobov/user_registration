from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from .serializers import PostSerializer, TagSerializer, BlogSerializer, CategorySerializer, CommentsSerializer
from main.models import Tag, Post, Category, Blog, Comments

class CreateTagView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer

class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer


class EditPostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
