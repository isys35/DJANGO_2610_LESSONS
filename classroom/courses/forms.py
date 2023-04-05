from django import forms
from django.core.exceptions import ValidationError
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput, TimePickerInput

from core.models import User

from courses import models
from courses import validators
from courses import consts
from courses.services import CreateLessonsService


class CourseForm(forms.ModelForm):
    started_at = forms.DateField(
        label="Начало курса",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y"),
        ),
        validators=[validators.validate_starte_date]
    )
    students = forms.ModelMultipleChoiceField(
        label="Учащиеся",
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        queryset=User.objects.all()
    )
    days_of_week = forms.MultipleChoiceField(
        label="Дни проведения занятий",
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        choices=consts.DaysOfWeek.choices
    )
    start_lesson_at = forms.TimeField(
        label="Время начала занятия",
        required=True,
        widget=TimePickerInput(
            options=FlatpickrOptions(altFormat="H:i"),
        )
    )
    end_lesson_at = forms.TimeField(
        label="Время окончания занятия",
        required=True,
        widget=TimePickerInput(
            range_from="start_lesson_at",
            options=FlatpickrOptions(altFormat="H:i"),
        )
    )

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if str(cleaned_data["started_at"].weekday()) not in cleaned_data["days_of_week"]:
            raise ValidationError("День недели должен совпадать с днем недели начала курса")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.request.user
        instance.save()
        # lesson_duration = self.cleaned_data["end_lesson_at"].hour - self.cleaned_data["start_lesson_at"].hour
        lessons = CreateLessonsService(
            start_lesson=self.cleaned_data["start_lesson_at"],
            end_lesson=self.cleaned_data["end_lesson_at"],
            first_lesson_date=self.cleaned_data["started_at"],
            # TODO: Проверить тип
            lesson_weekdays=[int(day) for day in self.cleaned_data["days_of_week"]],
            topics=instance.road_map.topics.all(),
            course=instance
        ).execute()
        lessons = models.CourseLesson.objects.bulk_create(lessons)
        students_lessons = []
        for lesson in lessons:
            for student in self.cleaned_data["students"]:
                student_lesson = models.StudentLesson(
                    lesson=lesson,
                    student=student
                )
                students_lessons.append(student_lesson)
        models.StudentLesson.objects.bulk_create(students_lessons)
        self._save_m2m()
        return instance

    class Meta:
        model = models.Course
        fields = (
            "name",
            "description",
            "started_at",
            "students",
            "road_map",
            "publicated"
        )


