from django import forms
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from courses import models
from courses import validators


class CourseForm(forms.ModelForm):
    started_at = forms.DateField(
        label="Начало курса",
        required=True,
        widget=DatePickerInput(
                options=FlatpickrOptions(altFormat="d.m.Y"),
            ),
        validators=[validators.validate_starte_date]
    )

    class Meta:
        model = models.Course
        fields = (
            "name",
            "description",
            "started_at"
        )