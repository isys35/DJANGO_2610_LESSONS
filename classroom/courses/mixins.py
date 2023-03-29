from django.forms.formsets import ORDERING_FIELD_NAME
from django.http import HttpResponseRedirect


class FormRequestKwargMixin:
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["request"] = self.request
        return form_kwargs


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
        return kwargs

    def form_valid(self, form, formset):
        # TODO: Refactor
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

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        kwargs["queryset"] = self.get_queryset().none()
        return kwargs


class UpdateRelatedFormSetMixin(RelatedFormSetMixin):
    related_name = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        kwargs["queryset"] = getattr(self.object, self.related_name).all()
        return kwargs