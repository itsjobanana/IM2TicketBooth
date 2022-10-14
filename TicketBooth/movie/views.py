from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View

from .forms import MovieForm


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




class success(View):
    template = 'success.html'
