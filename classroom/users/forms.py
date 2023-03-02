from django import forms
from django.contrib.auth.models import Group, Permission

from users.models import PermissionProxy


class GroupForm(forms.ModelForm):
    permissions =forms.ModelMultipleChoiceField(
        label="Курсы",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=PermissionProxy.objects.filter(content_type__model="course")
    )

    class Meta:
        model = Group
        fields = (
            "name",
            "permissions"
        )
