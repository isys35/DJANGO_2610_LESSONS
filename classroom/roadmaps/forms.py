from django import forms
from django.forms import BaseModelFormSet, modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME

from roadmaps import models


class RoadMapForm(forms.ModelForm):
    class Meta:
        model = models.RoadMap
        fields = (
            "name",
        )


class RoadMapBaseFormSet(BaseModelFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[ORDERING_FIELD_NAME].label = "Номер занятия"


RoadMapFormSet = modelformset_factory(
    models.Topic,
    formset=RoadMapBaseFormSet,
    fields=('name', "hours"),
    can_order=True,
)
