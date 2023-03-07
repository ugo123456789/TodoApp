from django.shortcuts import render
from .models import TODOlist


# Create your views here.

def index(request):
    todo_items = TODOlist.objects.order_by('id')
    context = {'todo_items':  todo_items}
    return render(request,'todolist/index.html', context)

