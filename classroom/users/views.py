from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from core import consts as core_consts
from django.contrib.auth.forms import UserCreationForm
from users import forms

class ListUsersView(ListView):
    context_object_name = "users"
    template_name = "auth/users/list.html"
    model = User
    paginate_by = core_consts.PAGE_SIZE


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "auth/users/create.html"
    success_url = reverse_lazy("users:list")
    success_message = "Запись успешно создана"


class ListGroupsView(ListView):
    context_object_name = "groups"
    template_name = "auth/groups/list.html"
    model = Group
    paginate_by = core_consts.PAGE_SIZE


class CreateGroupView(SuccessMessageMixin, CreateView):
    model = Group
    form_class = forms.GroupForm
    template_name = "auth/users/create.html"
    success_url = reverse_lazy("users:list")
    success_message = "Запись успешно создана"