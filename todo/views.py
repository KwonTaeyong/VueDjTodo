from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def TodoTV(request):
    return render(request,  'todo/todo_index.html')


def Toast(requset):
    return render(requset, 'todo/toast_grid.html')