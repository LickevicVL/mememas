from django.contrib.messages import add_message, ERROR
from django.shortcuts import redirect, reverse


class AccountModalMixin:
    form_name = None
    error_message = str()
    request = None

    def get(self, request, *args, **kwargs):
        return redirect(reverse('memes:index') + f'?form={self.form_name}')

    def form_invalid(self, form):
        path = self.request.GET.get('next', reverse('memes:index'))
        if self.error_message:
            add_message(
                self.request, ERROR, self.error_message, self.form_name
            )
        else:
            add_message(self.request, ERROR, form.errors, self.form_name)

        return redirect(f'{path}?form={self.form_name}')
