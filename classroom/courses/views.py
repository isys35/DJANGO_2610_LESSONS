import json

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from courses import forms
from courses import models
from courses import consts as courses_consts
from courses.mixins import FormRequestKwargMixin


class CoursesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "courses.view_course"
    context_object_name = "courses"
    template_name = "courses/list.html"
    queryset = models.Course.active_objects.get_related()
    paginate_by = courses_consts.PAGE_SIZE


class CourseCreateView(FormRequestKwargMixin,
                       PermissionRequiredMixin,
                       LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    permission_required = "courses.add_course"
    form_class = forms.CourseForm
    template_name = "courses/create.html"
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно создана"


class CourseDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "courses.view_course"
    model = models.Course
    template_name = "courses/detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data["comments"] = self.object.comments.all().annotate(count_likes=Count("likes")).select_related("author")
        return context_data



class CourseUpdateView(FormRequestKwargMixin,
                       PermissionRequiredMixin,
                       LoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    permission_required = "courses.change_course"
    model = models.Course
    template_name = "courses/update.html"
    form_class = forms.CourseForm
    success_message = "Запись успешно обновлена"


class CourseDeleteView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "courses.delete_course"
    model = models.Course
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно удалена"

    def get(self, *args, **kwargs):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return self.delete(*args, **kwargs)



def add_comment(request, pk):
    if request.method == "POST":
        course = models.Course.objects.get(id=pk)
        data_json = json.loads(request.body)
        comment_text = data_json.get("comment")
        comment = models.Comment.objects.create(
            content=comment_text,
            author=request.user,
            content_object=course
        )
        comment.count_likes = comment.likes.count()
        return render(request, "comment.html", {"comment": comment})
    return HttpResponse(status=405)


def add_comment_like(request, pk):
    if request.method == "POST":
        comment = models.Comment.objects.get(pk=pk)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return HttpResponse(comment.likes.count(), status=201)
    return HttpResponse(status=405)