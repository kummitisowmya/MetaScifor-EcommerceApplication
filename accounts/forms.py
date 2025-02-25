from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use our CustomUser instead of auth.User
        fields = ["username", "email", "password1", "password2","phone"]

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone"]