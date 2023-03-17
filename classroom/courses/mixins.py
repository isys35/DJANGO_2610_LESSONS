
class FormRequestKwargMixin:
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["request"] = self.request
        return form_kwargs