from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from courses import forms
from courses import models
from courses import consts as courses_consts


def courses_list(request):
    courses_qs = models.Course.objects.all()
    paginator = Paginator(courses_qs, courses_consts.PAGE_SIZE)
    page_number = request.GET.get("page") or 1
    page_courses = paginator.get_page(page_number)
    context = {"courses": page_courses}
    return render(request, "courses/list.html", context=context)


class CreateCourseView(View):
    form_class = forms.CourseForm
    template_name = "courses/create.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись успешно создана")
            return redirect("courses:list")
        return render(request, self.template_name, context={"form": form})



def course_detail(request, id):
    context = {"course": models.Course.objects.get(id=id)}
    return render(request, "courses/detail.html", context=context)


def course_update(request, id):
    course = models.Course.objects.get(id=id)
    if request.method == "POST":
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись успешно обновлена")
            return redirect("courses:detail", course.pk)
    form = forms.CourseForm(instance=course)
    context = {"form": form, "course": course}
    return render(request, "courses/update.html", context=context)


def course_delete(request, id):
    course = models.Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Запись успешно удалена")
    return redirect("courses:list")
