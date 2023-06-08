from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    todo = TodoItem.objects.all()
    print(todo)
    return render(request, 'todo.html', {"todo":todo})

def todoAdd(request):
    if request.method == "POST":
        new = TodoItem(content=request.POST["todocontent"])
        new.save()
        return HttpResponseRedirect("/")

def todoDelete(request, id):
    item = TodoItem.objects.get(id=id)
    print(id)
    item.delete()
    return HttpResponseRedirect("/")
