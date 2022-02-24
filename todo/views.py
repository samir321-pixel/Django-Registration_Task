from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='/login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    if request.method == "POST":
        query = Task.objects.create(user=request.user, title=request.POST.get('title'))
        context = {'tasks': tasks, 'form': form}
        return render(request, 'todo/list.html', context)
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/list.html', context)


@login_required(login_url='/login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/list/')
    context = {'form': form}
    return render(request, 'todo/update_task.html', context)


@login_required(login_url='/login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        form = TaskForm()
        return redirect('/tasks/list/', )
    context = {'item': item}
    return render(request, 'todo/delete.html', context)
