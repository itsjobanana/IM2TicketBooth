from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from bookticket.forms import ConcertBookingForm, MovieBookingForm


# Create your views here.

class HomeBookTicket(View):
    template = 'bookTicket_Index.html'

    def get(self, request):
        return render(request, self.template)


class MovieBookingTicket(View):
    template = 'bookTicket_Movie.html'

    def get(self, request):
        form = MovieBookingForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = MovieBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bookMovie:index'))
        return render(request, self.template, {'form': form})


class ConcertBookingTicket(View):
    template = 'bookTicket_Concert.html'

    def get(self, request):
        form = ConcertBookingForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ConcertBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bookConcert:index'))
        return render(request, self.template, {'form': form})
