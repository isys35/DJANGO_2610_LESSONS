from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(label="Название курса", max_length=100)
    description = forms.CharField(label="Описание")
    started_at = forms.DateField(label="Старт курса")
