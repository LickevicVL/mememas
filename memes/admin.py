from django.contrib import admin
from memes.models import Mem


@admin.register(Mem)
class MemAdmin(admin.ModelAdmin):
    exclude = ('slug',)
