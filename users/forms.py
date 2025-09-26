from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-md mt-2 px-4 py-1 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Username Here'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-md mt-2 px-4 py-1 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Your Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-md mt-2 px-4 py-1 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Confirm Password'
            }),
            }