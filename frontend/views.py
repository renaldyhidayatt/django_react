from django.shortcuts import render

from django.views.generic.detail import DetailView

from todos.models import Todo

def index(request):
    return render(request,'index.html')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'index.html'
