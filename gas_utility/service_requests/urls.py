from django.urls import path
from .views import create_request, request_list, request_detail

urlpatterns = [
    path('create/', create_request, name='create_request'),
    path('ticket_list', request_list, name='request_list'),
    path('<int:pk>/', request_detail, name='request_detail'),
]
