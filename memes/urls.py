from django.urls import path

from memes.views import index

urlpatterns = [
    path('', index, name='index'),
]
