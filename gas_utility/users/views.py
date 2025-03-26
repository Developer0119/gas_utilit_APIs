from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from service_requests.models import ServiceRequest
from support.models import SupportTicket
from .serializers import UserSerializer
from .forms import CustomUserCreationForm

User = get_user_model()


#  API: User Login (Session)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({"message": "User logged in successfully"}, status=200)
    return Response({"error": "Invalid credentials"}, status=400)

#  API: User Logout
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({"message": "User logged out successfully"}, status=200)

# API: Admin Dashboard
@api_view(['GET'])
@login_required
def dashboard_api(request):
    total_users = User.objects.count()
    total_requests = ServiceRequest.objects.count()
    total_tickets = SupportTicket.objects.count()

    return Response({
        "total_users": total_users,
        "total_requests": total_requests,
        "total_tickets": total_tickets
    })




