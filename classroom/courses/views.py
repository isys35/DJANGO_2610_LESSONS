from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from courses import forms
from courses import models
from courses import consts as courses_consts


class CoursesListView(ListView):
    model = models.Course
    template_name = "courses/list.html"
    paginate_by = courses_consts.PAGE_SIZE
    context_object_name = "courses"

# def courses_list(request):
#     courses_qs = models.Course.objects.all()
#     paginator = Paginator(courses_qs, courses_consts.PAGE_SIZE)
#     page_number = request.GET.get("page") or 1
#     page_courses = paginator.get_page(page_number)
#     context = {"courses": page_courses}
#     return render(request, "courses/list.html", context=context)


class CourseCreateView(View):
    form_class = forms.CourseForm

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.get(self, request)
        form.save()
        messages.success(request, "Курс успешно создан")
        return redirect("courses:list")

    def get(self, request):
        form = self.form_class()
        return render(request, "courses/create.html", context={"form": form})




def course_detail(request, id):
    context = {"course": models.Course.objects.get(id=id)}
    return render(request, "courses/detail.html", context=context)


def course_update(request, id):
    course = models.Course.objects.get(id=id)
    if request.method == "POST":
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Курс успешно обновлён")
            return redirect("courses:detail", course.id)
    else:
        form = forms.CourseForm(instance=course)
    return render(request, "courses/update.html", context={"form": form, "course": course})


def course_delete(request, id):
    models.Course.objects.get(id=id).delete()
    messages.success(request, "Курс успешно удалён")
    return redirect("courses:list")