from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
def main(request):
	all_tasks = Task.objects.all()
	return render(request, 'todo.html', {'all_tasks': all_tasks})
# Create your views here.
def add(request):
	task = request.POST['task']
	a = Task(alltasks=task)
	a.save()
	return HttpResponseRedirect('/')

def delete_obj(request, todo_id):
	item = Task.objects.get(id=todo_id)
	item.delete()
	return HttpResponseRedirect('/')
	