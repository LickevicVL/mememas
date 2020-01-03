from django import forms
from django.core.exceptions import ValidationError

from memes.models import Mem


class MemForm(forms.ModelForm):
    class Meta:
        model = Mem
        fields = ['title', 'body', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control-file'}
            )
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'mem' not in title.lower():
            raise ValidationError('Title must contain "mem".')

        return title


class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=True
    )

    def save(self, mem, user):
        body = self.cleaned_data['body']
        mem.comments.create(body=body, user=user)
