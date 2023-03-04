from django import forms
from django.contrib.auth.models import Group, Permission

from user_role.forms import UserCreationForm as AuthUserCreationForm
from user_role.models import User


class GroupCreationForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Permission.objects.filter(
            content_type__model__in=["course", "group", "user"],
        )
    )

    class Meta:
        model = Group
        fields = [
            "name",
            "permissions"
        ]


class UserCreationForm(AuthUserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "role"
        ]


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
