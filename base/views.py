from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from . import models
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'base/tasks.html'


class TaskDetail(DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    model = models.Task
    template_name = 'base/task_form.html'
    fields = '__all__'
    exclude = ['user']
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = models.Task
    template_name = 'base/task_form.html'
    fields = '__all__'
    exclude = ['user']
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = models.Task
    # template_name = 'base/task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
