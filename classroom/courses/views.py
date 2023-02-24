from django.core.paginator import Paginator
from django.shortcuts import render, redirect
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


def course_create(request):
    if request.method == "POST":
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses:list")
    else:
        form = forms.CourseForm()
    return render(request, "courses/create.html", context={"form": form})


def course_detail(request, id):
    context = {"course": models.Course.objects.get(id=id)}
    return render(request, "courses/detail.html", context=context)
