from django.contrib import messages
from django.forms.formsets import ORDERING_FIELD_NAME, DELETION_FIELD_NAME
from django.http import HttpResponseRedirect


class FormRequestKwargMixin:
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["request"] = self.request
        return form_kwargs


class FormSetMixin:

    def get_formset(self):
        return self.formset(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {}
        if self.request.method in ("POST", "PUT"):
            kwargs["data"] = self.request.POST
        else:
            kwargs["queryset"] = self.get_queryset().none()
        return kwargs

    def get_context_data(self, **kwargs):
        if "formset" not in kwargs:
            kwargs["formset"] = self.get_formset()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = self.get_formset()
        if form.is_valid() and formset.is_valid():
            return self.data_valid(form, formset)
        else:
            return self.data_invalid(form, formset)

    def data_valid(self, form, formset):
        self.object = form.save()
        for form in formset:
            related_instance = form.save(commit=False)
            if not form.cleaned_data:
                continue
            if form.cleaned_data[DELETION_FIELD_NAME]:
                related_instance.delete()
            related_instance.order = form.cleaned_data[ORDERING_FIELD_NAME]
            setattr(related_instance, self.related_instance_fk, self.object)
            related_instance.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())

    def data_invalid(self, form, formset):
        context_data = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context_data)


class CreateFormSetMixin(FormSetMixin):

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


class UpdateFormSetMixin(FormSetMixin):

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"queryset": self.object.topics.all()})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
