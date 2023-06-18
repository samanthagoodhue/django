# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task_list")


class Register(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            return redirect("login")
        return super(Register, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "task_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list"] = context["task_list"].filter(user=self.request.user)
        context["count"] = context["task_list"].filter(completed=False).count()
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = "create_task.html"
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = "update_task.html"
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateTask, self).form_valid(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = "delete_task.html"
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeleteTask, self).form_valid(form)
