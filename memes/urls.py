from django.urls import path

from memes import views

urlpatterns = [
    path('', views.ListMems.as_view(), name='index'),
    path('create/', views.CreateMem.as_view(), name='create_mem'),
    path('movies/', views.ListMovies.as_view(), name='movies'),
    path('<slug:slug>/', views.ViewMem.as_view(), name='mem'),
]
