from django.shortcuts import render, redirect
from courses import forms
from courses import models

def courses_list(request):
    return render(request, "courses/list.html")


def course_create(request):
    if request.method == "POST":
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            models.Course.objects.create(**form.cleaned_data)
            return redirect("courses:list")
        else:
            return render(request, "courses/create.html", context={"form": form})
    form = forms.CourseForm()
    return render(request, "courses/create.html", context={"form": form})
