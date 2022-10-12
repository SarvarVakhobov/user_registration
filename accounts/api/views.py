from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from accounts.models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer, ChangeUserDetailsSerializer
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(viewsets.ViewSet):
    def retrieve(self, request, pk):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CreateListUserView(APIView):
    def get(self, request):
        try:
            items = CustomUser.objects.all()
            serializer = UserSerializer(items, many=True)
        except Exception as e:
            return Response("There is not any user or Error")
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class ChangeUserDetailsView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = ChangeUserDetailsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

