from django.shortcuts import render, redirect
from courses import forms

def courses_list(request):
    return render(request, "courses/list.html")


def course_create(request):
    if request.method == "POST":
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            print("Форма валидна")
            return redirect("courses:list")
    form = forms.CourseForm()
    return render(request, "courses/create.html", context={"form": form})
