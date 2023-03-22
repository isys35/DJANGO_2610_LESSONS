from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Count, Sum
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from courses import forms
from courses import models
from courses import consts as courses_consts
from courses.forms import RoadMapFormSet
from courses.mixins import FormRequestKwargMixin


class CoursesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "courses.view_course"
    context_object_name = "courses"
    template_name = "courses/list.html"
    queryset = models.Course.objects.select_related("author").prefetch_related("users")
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


class RoadMapListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "courses.view_roadmap"
    context_object_name = "roadmaps"
    template_name = "courses/roadmaps/list.html"
    queryset = models.RoadMap.objects.all().annotate(
        count_topics=Count("topics"),
        count_hours=Sum("topics__hours")
    )
    paginate_by = courses_consts.PAGE_SIZE


class RelatedFormSetMixin:

    def get_context_data(self, **kwargs):
        if "formset" not in kwargs:
            kwargs["formset"] = self.get_formset()
        return super().get_context_data(**kwargs)

    def get_formset(self):
        return self.formset(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {}
        if self.request.method in ("POST", "PUT"):
            kwargs["data"] = self.request.POST
        else:
            kwargs["queryset"] = self.get_queryset().none()
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        for formset_item in formset:
            if not formset_item.cleaned_data:
                continue
            related_instance = formset_item.save(commit=False)
            setattr(related_instance, self.related_instance_fk, self.object)
            related_instance.order = formset_item.cleaned_data[ORDERING_FIELD_NAME]
            related_instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = self.get_formset()
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


class CreateRelatedFormSetMixin(RelatedFormSetMixin):

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


class UpdateRelatedFormSetMixin(RelatedFormSetMixin):
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class RoadMapCreateView(PermissionRequiredMixin,
                        LoginRequiredMixin,
                        CreateRelatedFormSetMixin,
                        CreateView):
    permission_required = "courses.add_roadmap"
    model = models.RoadMap
    form_class = forms.RoadMapForm
    template_name = "courses/roadmaps/create.html"
    success_url = reverse_lazy("courses:roadmap_list")
    success_message = "Запись успешно создана"
    related_instance_fk = "road_map"
    formset = RoadMapFormSet


class RoadMapDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "courses.view_roadmap"
    model = models.RoadMap
    template_name = "courses/roadmaps/detail.html"
    context_object_name = "roadmap"


class RoadMapUpdateView(PermissionRequiredMixin,
                        LoginRequiredMixin,
                        UpdateView):
    permission_required = "courses.change_roadmap"
    form_class = forms.RoadMapForm
    model = models.RoadMap
    template_name = "courses/roadmaps/update.html"
    success_url = reverse_lazy("courses:roadmap_list")
    success_message = "Запись успешно обновлена"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        context["formset"] = RoadMapFormSet(queryset=self.object.topics.all())
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = RoadMapFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            for topic_form in formset:
                if not topic_form.cleaned_data:
                    continue
                topic = topic_form.save(commit=False)
                topic.road_map = self.object
                topic.order = topic_form.cleaned_data[ORDERING_FIELD_NAME]
                topic.save()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)
