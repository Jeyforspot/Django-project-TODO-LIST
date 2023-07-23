from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Task
from .forms import TaskCreateForm


def render_main_page(request):
    context = {}
    return render(request, 'main_page.html', context)


class TaskListView(ListView):
    template_name = 'ToDoList/all_tasks.html'
    model = Task
    context = {'f': 'ggg'}


class TaskCreateView(CreateView):
    template_name = 'ToDoList/create_task.html'
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse('ToDoList:task-list')
