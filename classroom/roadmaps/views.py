from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from roadmaps import models, consts, forms
from roadmaps.mixins import CreateRelatedFormSetMixin, UpdateRelatedFormSetMixin


class RoadMapListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "roadmaps.view_roadmap"
    context_object_name = "roadmaps"
    template_name = "roadmaps/list.html"
    queryset = models.RoadMap.objects.all().annotate(
        count_topics=Count("topics"),
        count_hours=Sum("topics__hours")
    )
    paginate_by = consts.PAGE_SIZE


class RoadMapCreateView(PermissionRequiredMixin,
                        LoginRequiredMixin,
                        CreateRelatedFormSetMixin,
                        CreateView):
    permission_required = "roadmaps.add_roadmap"
    model = models.RoadMap
    form_class = forms.RoadMapForm
    template_name = "roadmaps/create.html"
    success_url = reverse_lazy("roadmaps:list")
    success_message = "Запись успешно создана"
    related_instance_fk = "road_map"
    formset = forms.RoadMapFormSet


class RoadMapDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "roadmaps.view_roadmap"
    model = models.RoadMap
    template_name = "roadmaps/detail.html"
    context_object_name = "roadmap"


class RoadMapUpdateView(PermissionRequiredMixin,
                        LoginRequiredMixin,
                        UpdateRelatedFormSetMixin,
                        UpdateView):
    permission_required = "roadmaps.change_roadmap"
    form_class = forms.RoadMapForm
    model = models.RoadMap
    template_name = "roadmaps/update.html"
    success_url = reverse_lazy("roadmaps:list")
    success_message = "Запись успешно обновлена"
    formset = forms.RoadMapFormSet
    related_name = "topics"
    related_instance_fk = "road_map"
