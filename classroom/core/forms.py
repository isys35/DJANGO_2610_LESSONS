from django import forms
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.contrib.auth.models import Permission
from user_role.models import Role

from core.models import User
from core.widgets import PermissionsSelectMultiply


class RoleCreationForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        widget=PermissionsSelectMultiply(),
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Role
        fields = [
            "name",
            "permissions"
        ]


class UserCreationForm(AuthUserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Подтвержение пароля",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False
    )
    role = forms.ModelChoiceField(
        label="Роль",
        queryset=Role.objects.all(),
        required=False,
        widget=forms.Select()
    )



    class Meta:
        model = User
        fields = [
            "email",
            "role",
            "first_name",
            "last_name",
            "photo"
        ]
        required = (
            "first_name",
            "last_name"
        )


class UserUpdateForm(forms.ModelForm):
    role = forms.ModelChoiceField(
        label="Роль",
        queryset=Role.objects.all(),
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = [
            "email",
            "role",
            "first_name",
            "last_name",
            "photo"
        ]
