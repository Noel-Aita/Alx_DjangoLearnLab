from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token


from .serializers import (
    RegisterSerializer,
    UserPublicSerializer,
    ProfileUpdateSerializer,
)


User = get_user_model()


class RegisterView(APIView):
    # POST /register — Create a new user and return an auth token."""

    permission_classes = [permissions.AllowAny]


def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Create a token for the new user
        token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {
            "token": token.key,
            "user": UserPublicSerializer(user, context={"request": request}).data,
        },
        status=status.HTTP_201_CREATED,
    )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    # POST /login — Authenticate credentials and return a token + user info."""

    permission_classes = [permissions.AllowAny]


def post(self, request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"detail": "username and password are required"}, status=400)

    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({"detail": "Invalid credentials"}, status=400)

    token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {
            "token": token.key,
            "user": UserPublicSerializer(user, context={"request": request}).data,
        }
    )


class ProfileView(generics.RetrieveUpdateAPIView):
    {}
