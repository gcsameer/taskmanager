

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Task

# ----------------------------
# User Registration
# ----------------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('task_list')
    return render(request, 'register.html')

# ----------------------------
# User Login
# ----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
    return render(request, 'login.html')

# ----------------------------
# User Logout
# ----------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

# ----------------------------
# Task List
# ----------------------------
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# ----------------------------
# Create Task
# ----------------------------
@login_required
def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(user=request.user, title=title)
        return redirect('task_list')
    return render(request, 'task_form.html')

# ----------------------------
# Update Task
# ----------------------------
@login_required
def task_update(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

# ----------------------------
# Delete Task
# ----------------------------
@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('task_list')

# ----------------------------
# Mark as Complete
# ----------------------------
@login_required
def task_complete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')
