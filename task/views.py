from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm


# tasks = [
#     {'id': 1, 'text': 'Learn Python'},
#     {'id': 2, 'text': 'Learn Django'},
#     {'id': 3, 'text': 'Build something amazing'},
# ]

def index(request):
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'tasks': tasks})


def task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task.html', {'task': task})


@login_required(login_url='login')
def new_task(request):
    task_form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect('index')
    return render(request, 'task/new.html', {'task_form': task_form})


@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('index')
    return render(request, 'task/edit.html', {'task_form': task_form, 'task': task})


@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, "Task deleted successfully!")
