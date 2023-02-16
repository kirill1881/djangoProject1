from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def add_task(request):
    return render(request, 'addTask.html')

def edit_task(request):
    return render(request, 'editTask.html')
