from django import forms
from django.forms.utils import ErrorList


class FormUserMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.User = self.request.user
            return super(FormUserMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['You need be logged'])
            return self.form_invalid(form)
