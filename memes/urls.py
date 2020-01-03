from django.urls import path

from memes import views
from memes.utils import NEW, HOT

urlpatterns = [
    path('', views.ListMems.as_view(), {'ordering': NEW}, name='index'),
    path('hot/', views.ListMems.as_view(), {'ordering': HOT}, name='hot'),
    path('create/', views.CreateMem.as_view(), name='create_mem'),
    path('movies/', views.ListMovies.as_view(), name='movies'),
    path('<slug:slug>/', views.ViewMem.as_view(), name='mem'),
    path('<slug:slug>/comment/', views.CreateComment.as_view(), name='comment')
]
