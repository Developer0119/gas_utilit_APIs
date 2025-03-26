from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser  # Ensure the correct import

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Ensure this is correct
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'address']
