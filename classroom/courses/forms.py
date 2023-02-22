from django import forms
from courses import models


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = (
            "name",
            "description",
            "started_at"
        )

