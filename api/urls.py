from django.urls import path
from api import views


urlpatterns = [
    path('mem', views.MemApi.as_view())
]
