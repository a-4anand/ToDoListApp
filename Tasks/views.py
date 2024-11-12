from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import render



# View to list all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/view_task.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        # Check if the fields exist in the POST request
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')

        # Validate the fields and create a new task
        if title and description:
            new_task = Task(title=title, description=description)
            new_task.save()
            return redirect('task_list')
        else:
            # If fields are missing, return an error or render the form with an error message
            return render(request, 'add_task.html', {'error': 'Please fill in all fields.'})

    return render(request, 'tasks/add_task.html')

# View to mark task as completed
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# View to delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# Edit the task details
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

