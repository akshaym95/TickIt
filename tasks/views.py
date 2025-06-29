from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    """Display all tasks for the logged-in user"""
    tasks = Task.objects.filter(user=request.user)
    
    # Filter by status
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_type == 'pending':
        tasks = tasks.filter(completed=False)
    
    context = {
        'tasks': tasks,
        'filter_type': filter_type,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
    """Create a new task"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Create New Task'})

@login_required
def task_detail(request, pk):
    """Display task details"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_edit(request, pk):
    """Edit an existing task"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form, 
        'task': task,
        'title': 'Edit Task'
    })

@login_required
def task_delete(request, pk):
    """Delete a task"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('tasks:task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle(request, pk):
    """Toggle task completion status"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'completed': task.completed,
            'completed_at': task.completed_at.isoformat() if task.completed_at else None
        })
    
    messages.success(request, f'Task marked as {"completed" if task.completed else "pending"}!')
    return redirect('tasks:task_list')
