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
            }
        
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)

            self.fields['password1'].widget.attrs.update({
                'class': 'w-md mt-2 px-4 py-1 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Your Password'
            })

            self.fields['password2'].widget.attrs.update({
                'class': 'w-md mt-2 px-4 py-1 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Confirm Your Password'
            })