from django.urls import path, include

from .views import RegisterView, UserDetailView, CreateListUserView, ChangePasswordView, MyTokenObtainPairView, ChangeUserDetailsView
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('userlist/', CreateListUserView.as_view(), name='userlist'),
    path('userdetails/<int:pk>/', UserDetailView.as_view({'get': 'retrieve'}), name='userdetails'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    path('change_userdetails/<int:pk>/', ChangeUserDetailsView.as_view(), name='change_userdetails')
]