from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Sum
from django.forms.formsets import ORDERING_FIELD_NAME
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from courses import forms
from courses import models
from courses import consts as courses_consts
from courses.mixins import FormRequestKwargMixin, CreateFormSetMixin


class CoursesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "courses.view_course"
    context_object_name = "courses"
    template_name = "courses/list.html"
    queryset = models.Course.objects.select_related("author").prefetch_related("users")
    paginate_by = courses_consts.PAGE_SIZE


class CreateCourseView(FormRequestKwargMixin,
                       PermissionRequiredMixin,
                       LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    permission_required = "courses.add_course"
    form_class = forms.CourseForm
    template_name = "courses/create.html"
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно создана"


class DetailCourseView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "courses.view_course"
    model = models.Course
    template_name = "courses/detail.html"
    context_object_name = "course"


class UpdateCourseView(FormRequestKwargMixin,
                       PermissionRequiredMixin,
                       LoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    permission_required = "courses.change_course"
    model = models.Course
    template_name = "courses/update.html"
    form_class = forms.CourseForm
    success_message = "Запись успешно обновлена"


class DeleteCourseView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "courses.delete_course"
    model = models.Course
    success_url = reverse_lazy("courses:list")
    success_message = "Запись успешно удалена"

    def get(self, *args, **kwargs):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return self.delete(*args, **kwargs)


class RoadMapListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "courses.view_roadmap"
    context_object_name = "roadmaps"
    template_name = "courses/roadmaps/list.html"
    queryset = models.RoadMap.objects.all().annotate(count_topics=Count("topics"), count_hours=Sum("topics__hours"))
    paginate_by = courses_consts.PAGE_SIZE


class CreateRoadMapView(PermissionRequiredMixin,
                        LoginRequiredMixin,
                        CreateFormSetMixin,
                        CreateView):
    permission_required = "courses.add_roadmap"
    form_class = forms.RoadMapForm
    model = models.RoadMap
    template_name = "courses/roadmaps/create.html"
    success_url = reverse_lazy("courses:roadmap_list")
    success_message = "Запись успешно создана"
    formset = forms.RoadMapFormset
    related_instance_fk = "road_map"


class DetailRoadMapView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "courses.view_roadmap"
    model = models.RoadMap
    template_name = "courses/roadmaps/detail.html"
    context_object_name = "roadmap"


class UpdateRoadMapView(PermissionRequiredMixin, LoginRequiredMixin, UpdateFormSetMixin, UpdateView):
    permission_required = "courses.change_roadmap"
    model = models.RoadMap
    template_name = "courses/roadmaps/update.html"
    context_object_name = "roadmap"
    form_class = forms.RoadMapForm
    success_url = reverse_lazy("courses:roadmap_list")
    success_message = "Запись успешно создана"
    formset = forms.RoadMapFormset
    related_instance_fk = "road_map"
