import requests
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
            raise ValidationError('Title must contain "mem".')

        return title

    def clean_url(self):
        url = self.cleaned_data['url']

        try:
            response = requests.get(url)
        except requests.ConnectionError:
            raise forms.ValidationError('Not valid url.')

        content_type = response.headers.get('Content-Type', '')

        if content_type.split('/')[0] != 'image':
            raise forms.ValidationError('Not a valid image.')

        return url
