from django import forms
from django.forms import modelformset_factory, BaseModelFormSet
from django.forms.formsets import ORDERING_FIELD_NAME
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from core.models import User

from courses import models
from courses import validators


class BaseRoadMapFormSet(BaseModelFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[ORDERING_FIELD_NAME].label = "Порядок занятия"


RoadMapFormset = modelformset_factory(
    models.Topic,
    formset=BaseRoadMapFormSet,
    fields=('name', "hours"),
    can_order=True,
)


class CourseForm(forms.ModelForm):
    started_at = forms.DateField(
        label="Начало курса",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y"),
        ),
        validators=[validators.validate_starte_date]
    )
    users = forms.ModelMultipleChoiceField(
        label="Учащиеся",
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        queryset=User.objects.all()
    )

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.request.user
        instance.save()
        self._save_m2m()
        return instance

    class Meta:
        model = models.Course
        fields = (
            "name",
            "description",
            "started_at",
            "users"
        )


class RoadMapForm(forms.ModelForm):
    class Meta:
        model = models.RoadMap
        fields = (
            "name",
        )
