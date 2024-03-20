from django.shortcuts import render
from new.models import *

# Create your views here.
def todo(request):
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    if request.method=='POST':
        title=request.POST.get('title')
        des=request.POST.get('des')
        if title and des:
            info=Todo(title=title,des=des)
            info.save()
    elif request.method=='GET':
        sno=request.GET.get('sno')
        Todo.objects.filter(sno=sno).delete()
        alltodos=Todo.objects.all()
        d={'alltodos':alltodos}
        return render(request, 'todo.html',d)

    return render(request,'todo.html',d)

sno=0
def update(request):
    if request.method=='GET':
        global sno
        sno=request.GET.get('sno')
        return render(request,'update.html')
    elif request.method=='POST':
        title=request.POST.get('title')
        des=request.POST.get('des')
        Todo.objects.filter(sno=sno).update(title=title,des=des)
        alltodos=Todo.objects.all()
        d={'alltodos':alltodos}
        return render(request, 'todo.html',d)
    return render(request,'update.html')
