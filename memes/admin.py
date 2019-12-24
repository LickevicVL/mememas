from django.contrib import admin
from django.shortcuts import reverse

from memes.models import Mem


@admin.register(Mem)
class MemAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.site_url = reverse('memes:index')
