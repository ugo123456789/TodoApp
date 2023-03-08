from django.shortcuts import render, redirect
from .models import TODOlist
from .forms import TodoListForm
from django.views.decorators.http import require_POST



# Create your views here.

def index(request):
    todo_items = TODOlist.objects.order_by('id')
    form  = TodoListForm()
    context = {'todo_items':  todo_items, 'form': form}
    return render(request,'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = TODOlist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedItems(request, todo_id):
    todo = TODOlist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    TODOlist.objects.filter(completed=True).delete()
    return redirect('index')

def deleteAll(request):
    TODOlist.objects.filter().delete()
    return redirect('index')

