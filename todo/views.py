from django.shortcuts import render, redirect, HttpResponse
from .models import Task

# Create your views here.
def index(request):
    return HttpResponse("This is Index Page")

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        completed = request.POST.get('completed') == 'on'

        task = Task(title=title, content=content, completed=completed)
        task.save()

        return redirect('task-list')  # Redirect to the task list view

    return render(request, 'add_task.html')

# def task(request):