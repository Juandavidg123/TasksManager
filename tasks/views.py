from django.shortcuts import render, get_object_or_404
from .forms import createTaskForm
from django.shortcuts import redirect
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tasks(request):
    listTasksCompleted = Task.objects.filter(user=request.user, completed=True).order_by('-date_completed')
    listTasksNotImportant = Task.objects.filter(user=request.user, completed=False, important=False).order_by('created_date')
    listTasksImportant = Task.objects.filter(user=request.user, completed=False, important=True).order_by('created_date')
    return render(request, 'tasks.html', {
        'taskscompleted': listTasksCompleted,
        'notimportant': listTasksNotImportant,
        'important': listTasksImportant
    })

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': createTaskForm()
        })
    else:
        try:
            form = createTaskForm(request.POST)
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {
                'form': createTaskForm(),
                'error': 'Invalid data. Try again.'
            })

@login_required
def detail(request, taskid):
    task = get_object_or_404(Task, pk=taskid)
    return render(request, 'detail.html',{
        'task': task
    })

@login_required
def update(request, taskid):
    task = get_object_or_404(Task, pk=taskid, user=request.user)
    if request.method == 'GET':
        form = createTaskForm(instance=task)
        return render(request, 'update.html', {
            'form': form,
            'task': task
        })
    else:
        try:
            form = createTaskForm(request.POST, instance=task)
            form.save()
            return redirect('detail', taskid=taskid)
        except:
            return render(request, 'update.html', {
            'form': form,
            'task': task,
            'error': 'Invalid data. Try again.'
        })

@login_required
def completed(request, taskid):
    task = get_object_or_404(Task, pk=taskid, user=request.user)
    if request.method == 'POST':
        task.completed = True
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def deleted(request, taskid):
    return render(request, 'delete.html', {
        'task': get_object_or_404(Task, pk=taskid, user=request.user)
    })

@login_required
def deletetask(request, taskid):
    task = get_object_or_404(Task, pk=taskid, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
