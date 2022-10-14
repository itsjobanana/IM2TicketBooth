from . import views
from django.urls import path

app_name = 'movie'

urlpatterns = [
    path('', views.HomeView.as_view(), name='movie_index'), #127.0.0.1/movie/
    path('addMovie', views.addMovie.as_view(), name='add_movie'), #127.0.0.1/movie/addMovie/
    path('success', views.success.as_view(), name='success'),
]
