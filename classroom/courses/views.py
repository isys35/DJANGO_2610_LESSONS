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
from courses.mixins import FormRequestKwargMixin


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
                        SuccessMessageMixin,
                        CreateView):
    permission_required = "courses.add_roadmap"
    form_class = forms.RoadMapForm
    template_name = "courses/roadmaps/create.html"
    success_url = reverse_lazy("courses:roadmap_list")
    success_message = "Запись успешно создана"

    def get_formset(self):
        return forms.RoadMapFormset(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {}
        if self.request.method in ("POST", "PUT"):
            kwargs["data"] = self.request.POST
        else:
            kwargs["queryset"] = models.RoadMap.objects.none()
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.get_formset()
        if form.is_valid() and formset.is_valid():
            return self.data_valid(form, formset)
        else:
            return self.data_invalid(form, formset)

    def get_context_data(self, **kwargs):
        if "formset" not in kwargs:
            kwargs["formset"] = self.get_formset()
        return super().get_context_data(**kwargs)

    def data_valid(self, form, formset):
        self.object = form.save()
        for form in formset:
            topic = form.save(commit=False)
            if form.cleaned_data:
                topic.order = form.cleaned_data[ORDERING_FIELD_NAME]
                topic.road_map = self.object
                topic.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())

    def data_invalid(self, form, formset):
        context_data = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context_data)


class DetailRoadMapView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "courses.view_roadmap"
    model = models.RoadMap
    template_name = "courses/roadmaps/detail.html"
    context_object_name = "roadmap"
