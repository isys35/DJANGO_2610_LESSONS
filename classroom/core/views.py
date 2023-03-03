from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from core.consts import PAGE_SIZE
from core.forms import GroupCreationForm, UserCreationForm, UserUpdateForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "base.html"


class UserListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "core.view_users"
    context_object_name = "users"
    template_name = "core/users/list.html"
    model = User
    paginate_by = PAGE_SIZE


class UserCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "core.add_users"
    form_class = UserCreationForm
    template_name = "core/users/create.html"
    success_url = reverse_lazy("core:users_list")
    success_message = "Пользователь успешно создан"


class UserUpdateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "core.change_users"
    form_class = UserUpdateForm
    model = User
    template_name = "core/users/update.html"
    success_url = reverse_lazy("core:users_list")
    success_message = "Пользователь успешно обновлен"


class GroupListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "core.view_groups"
    context_object_name = "groups"
    template_name = "core/groups/list.html"
    model = Group
    paginate_by = PAGE_SIZE


class GroupCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "core.add_groups"
    form_class = GroupCreationForm
    template_name = "core/groups/create.html"
    success_url = reverse_lazy("core:group_list")
    success_message = "Группа успешно создана"
