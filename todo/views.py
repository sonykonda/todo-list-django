from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-created')

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'home.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/')
