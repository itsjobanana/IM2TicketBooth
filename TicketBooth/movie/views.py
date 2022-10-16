from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from registration.models import Movie
from .forms import MovieForm, EditMovieForm


# Create your views here.
class HomeView(View):
    template = 'index_movie.html'

    def get(self, request):
        return render(request, self.template)


class addMovie(View):
    template = 'addMovie.html'

    def get(self, request):
        form = MovieForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "success.html")

class MovieList(View):
    template = 'movielistA.html'

    def get(self, request):
        movielist = Movie.objects.all()
        return render(request, self.template, {'Movie': movielist})

class MovieListU(View):
    template = 'movielistU.html'

    def get(self, request):
        movielistu = Movie.objects.all()
        return render(request, self.template, {'Movie': movielistu})


class EditMovie(View):
    template = 'editMovie.html'

    def get(self, request, id):
        concert = Movie.objects.get(pk=int(id))
        editmovie = EditMovieForm(instance=concert)
        return render(request, self.template, {'editmovie': editmovie})

    def post(self, request, id):
        movie = Movie.objects.get(pk=int(id))
        form = EditMovieForm(request.POST, instance=movie)
        if form.is_valid:
            form.save()
        return redirect(reverse('movie:movielistA'))

class deletemovie(View):
    template = 'movielistA.html'

    def get(self, request, id):
        delmovie = Movie.objects.get(pk=int(id))
        delete = MovieForm(instance=delmovie)
        delmovie.delete()
        return redirect(reverse('movie:movielistA'))
        return render(request, self.template, {'delete': delete})



class success(View):
    template = 'success.html'
