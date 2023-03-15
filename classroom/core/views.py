from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from user_role.forms import RoleCreationForm
from user_role.models import Role

from core.consts import PAGE_SIZE
from core.forms import UserCreationForm, UserUpdateForm
from core.models import User


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


class RoleListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "user_role.view_role"
    context_object_name = "roles"
    template_name = "core/roles/list.html"
    model = Role
    paginate_by = PAGE_SIZE


class RoleCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "user_role.add_role"
    form_class = RoleCreationForm
    template_name = "core/roles/create.html"
    success_url = reverse_lazy("core:role_list")
    success_message = "Роль успешно создана"
