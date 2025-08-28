from django.shortcuts import render, get_object_or_404 , redirect

from django_filters.rest_framework import DjangoFilterBackend

from .models import TodoTask
from .forms import TodoTaskForm
from .filters import TodoTaskFilter

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    todos = TodoTask.objects.filter(user=request.user, is_completed=False)
    completed_todos = TodoTask.objects.filter(user=request.user, is_completed=True)
    return render(request, 'home.html', {'todos': todos, 'completed_todos': completed_todos})

@login_required
def completed(request, id):
    todo = TodoTask.objects.get(id=id)
    todo.is_completed = True
    todo.save()
    return redirect(home)

@login_required
def deleted(request, id):
    todo = TodoTask.objects.get(id=id)
    todo.delete()
    return redirect(home)  

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title and due_date:
            TodoTask.objects.create(user=request.user, title=title, due_date=due_date)
    return redirect('home')  # Replace 'home' with your actual URL name

@login_required 
def edit_todo(request, id):
    todo = get_object_or_404(TodoTask, id=id, user=request.user)
    
    if request.method == 'POST':
        form = TodoTaskForm(request.POST, instance=todo)  # Pass the existing task to the form
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = TodoTaskForm(instance=todo)  # Pre-fill the form with the existing task data

    return render(request, 'edit.html', {'form': form})  

# views.py
from rest_framework import viewsets
from .serializers import TodoTaskSerializer

class TodoTaskViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoTaskFilter

# def update_todo(request, id):
#     if request.method == 'POST':
#         todo = TodoTask.objects.get(id=id)
#         todo.title = request.POST.get('title')
#         todo.due_date = request.POST.get('due_date')
#         todo.save()
#         return redirect('home')
#     return redirect('home')

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


from django.conf import settings

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 🔽 Explicitly set backend, since you have multiple
            from django.contrib.auth import authenticate
            user.backend = 'todoapp.backends.EmailAuthBackend'

            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


from .forms import StickyNoteForm
from .models import StickyNote

@login_required
def sticky_notes(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('sticky_notes')
    else:
        form = StickyNoteForm()

    notes = StickyNote.objects.filter(user=request.user)
    return render(request, 'sticky_notes.html', {'form': form, 'notes': notes})
