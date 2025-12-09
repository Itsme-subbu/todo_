from django.shortcuts import render
from todo_app.models import Task
# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    incompleteTasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks': tasks,
        'incompleteTask' : incompleteTasks
    }

    return render(request, 'home.html', context)