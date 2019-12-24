from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.views.generic import FormView

from accounts.forms import MemAuthenticationForm, MemUserCreationForm
from accounts.mixins import AccountModalMixin


class MemLoginView(AccountModalMixin, LoginView):
    form_name = 'login'
    error_message = 'Invalid username or password'
    form_class = MemAuthenticationForm


class MemUserCreationView(AccountModalMixin, FormView):
    form_name = 'register'
    form_class = MemUserCreationForm

    def form_valid(self, form):
        form.save()

        path = self.request.GET.get('next', reverse('memes:index'))
        self.success_url = f'{path}?form={MemLoginView.form_name}'

        return super().form_valid(form)
