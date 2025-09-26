from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import Task
from . froms import TaskFrom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# Create your views here.
@login_required
def task_list(request):
    status_filter = request.GET.get('status', 'all')
    category_filter = request.GET.get('category', 'all')
    
    tasks = Task.objects.filter(user = request.user)
    
    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))
        
    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)
        
        
    completed_task = tasks.filter(is_completed = True)
    pending_task = tasks.filter(is_completed = False)
    
    return render(request, 'task_list.html',{
        'status_filter' : status_filter,
        'category_filter' : category_filter,
        'completed_task' : completed_task,
        'pending_task' : pending_task
    })
    

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskFrom()
    return render(request, 'task_create.html', {'form' : form})
    

@login_required    
def task_detail(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    return render(request, '', {'task' : task})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    task.delete()
    return redirect('task_list')

@login_required
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')


# def Register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data.get('username')
#             # password = form.cleaned_data.get('password')
#             # user = authenticate(username = username, password = password)
#             # login(request, user)
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'User Created Successfully')
#             return redirect('task_list')
#     else:
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form' : form})
    
    