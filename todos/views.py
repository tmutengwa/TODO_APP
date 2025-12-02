from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import TODO

# Create your views here.

def home(request):
    """Display all TODO items"""
    todos = TODO.objects.all()
    return render(request, 'todos/home.html', {'todos': todos})

def create_todo(request):
    """Create a new TODO item"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')

        todo = TODO(title=title, description=description)
        if due_date:
            todo.due_date = due_date
        todo.save()
        return redirect('home')
    return render(request, 'todos/create.html')

def edit_todo(request, todo_id):
    """Edit an existing TODO item"""
    todo = get_object_or_404(TODO, id=todo_id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')
        if due_date:
            todo.due_date = due_date
        else:
            todo.due_date = None
        todo.save()
        return redirect('home')

    return render(request, 'todos/edit.html', {'todo': todo})

def delete_todo(request, todo_id):
    """Delete a TODO item"""
    todo = get_object_or_404(TODO, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'todos/delete.html', {'todo': todo})

def toggle_resolved(request, todo_id):
    """Toggle the resolved status of a TODO item"""
    todo = get_object_or_404(TODO, id=todo_id)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect('home')
