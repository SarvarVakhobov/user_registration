from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from .serializers import PostSerializer, TagSerializer, BlogSerializer, CategorySerializer, CommentsSerializer
from main.models import Tag, Post, Category, Blog, Comments
from accounts.api.permissions import OnlyAdmin, AdminAndModirator, AdminModiratorAndEditor

class TagListView(APIView):
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    def get(self, request):
        try:
            tags = Tag.objects.all()
            serializer = Tag(items, many=True)
        except Exception as e:
            return Response("There is not any tag or Error")
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateTagView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    serializer_class = TagSerializer

class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    serializer_class = PostSerializer

class PostView(APIView):
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post)
        except Exception as e:
            return Response("There is not any post like this or Error")
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostListView(APIView):
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    def get(self, request):
        try: 
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
        except Exception as e:
            return Response("There is not any post or Error")
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditPostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (AdminModiratorAndEditor, IsAuthenticated)
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
