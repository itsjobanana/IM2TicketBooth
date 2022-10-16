from . import views
from django.urls import path

app_name = 'movie'

urlpatterns = [
    path('', views.HomeView.as_view(), name='movie_index'), #127.0.0.1/movie/
    path('addMovie', views.addMovie.as_view(), name='add_movie'), #127.0.0.1/movie/addMovie/
    path('success', views.success.as_view(), name='success'),
    path('movielistA', views.MovieList.as_view(), name='movielistA'),
    path('editmovie/<int:id>', views.EditMovie.as_view(), name='editmovie'),
    path('deletemovie/<int:id>', views.deletemovie.as_view(), name='deletemovie'),
    path('movielistU', views.MovieListU.as_view(), name='movielistU'),

]
