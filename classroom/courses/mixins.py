from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy


class BasePermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy("core:login")
