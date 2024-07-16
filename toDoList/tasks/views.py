from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm



def index(request):
    """Vista para la página de inicio."""
    return render(request, 'tasks/index.html')

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(comit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        
        else:
            form = TaskForm()
        return render(request, 'tasks/task_form.html', {'form': form})
    

def task_edit(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
         form = TaskForm(request.POST, instance=task)
         if form.is_valid():            form.save()
         return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def signup(request):
    """Registrar un nuevo usuario."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})