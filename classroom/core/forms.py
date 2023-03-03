from django import forms
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.contrib.auth.models import Group, Permission, User


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
    groups = forms.ModelChoiceField(
        label="Группа",
        queryset=Group.objects.all(),
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = [
            "username",
            "groups"
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
            "username",
            "groups"
        ]