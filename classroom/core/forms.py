from django import forms
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.contrib.auth.models import Group, Permission
from user_role.models import Role

from core.models import User


class RoleCreationForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Permission.objects.filter(
            content_type__model__in=["course", "group", "user"],
        )
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
    groups = forms.ModelChoiceField(
        label="Группа",
        queryset=Group.objects.all(),
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = [
            "email",
            "groups",
            "first_name",
            "last_name"
        ]
        required = (
            "first_name",
            "last_name"
        )


class UserUpdateForm(forms.ModelForm):
    groups = forms.ModelChoiceField(
        label="Группа",
        queryset=Group.objects.all(),
        required=False,
        widget=forms.Select()
    )

    def _save_m2m(self):
        if groups := self.cleaned_data.get("groups"):
            self.cleaned_data["groups"] = [groups]
        else:
            self.cleaned_data["groups"] = []
        return super()._save_m2m()

    class Meta:
        model = User
        fields = [
            "email",
            "groups"
        ]
