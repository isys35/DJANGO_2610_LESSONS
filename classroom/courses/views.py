from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from courses import forms
from courses import models
from courses import consts as courses_consts


class CoursesListView(ListView):
    context_object_name = "courses"
    template_name = "courses/list.html"
    model = models.Course
    paginate_by = courses_consts.PAGE_SIZE


class CreateCourseView(SuccessMessageMixin, CreateView):
    form_class = forms.CourseForm
    template_name = "courses/create.html"
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно создана"


class DetailCourseView(DetailView):
    model = models.Course
    template_name = "courses/detail.html"
    context_object_name = "course"


class UpdateCourseView(SuccessMessageMixin, UpdateView):
    model = models.Course
    template_name = "courses/update.html"
    form_class = forms.CourseForm
    success_message = "Запись успешно обновлена"


class DeleteCourseView(SuccessMessageMixin, DeleteView):
    model = models.Course
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно удалена"
