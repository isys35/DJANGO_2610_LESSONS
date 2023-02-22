from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(label="Название курса", max_length=100)
    description = forms.CharField(label="Описание", required=False)
    started_at = forms.DateField(label="Старт курса", widget=forms.DateInput)
