from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def Register_view(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User Created Successfully')
            return redirect('task_list')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})
    
    
    
def Login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully')
                return redirect('task_list')
            else:
                messages.success(request, 'Invalid Creadintial')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})


def Logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')