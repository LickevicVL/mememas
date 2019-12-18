from django.urls import path

from memes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.view_mem, name='mem'),
    path('create/', views.create_mem, name='create_mem'),
]
