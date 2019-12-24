from accounts.forms import MemAuthenticationForm, MemUserCreationForm


def account_context(request):
    return {
        'login_form': MemAuthenticationForm(),
        'register_form': MemUserCreationForm()
    }
