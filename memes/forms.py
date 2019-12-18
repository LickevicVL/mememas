from django import forms
from django.core.exceptions import ValidationError
from memes.models import Mem


class MemForm(forms.ModelForm):
    class Meta:
        model = Mem
        fields = ['title', 'body', 'url']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'mem' not in title.lower():
            raise ValidationError('Title must contain "mem"')

        return title
