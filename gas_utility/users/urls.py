from django.urls import path
from .views import  user_login, user_logout, dashboard_api

urlpatterns = [
   
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard_api, name='dashboard-api'),
]

