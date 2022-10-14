from django.db import connection

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import *
from .models import *

# Create your views here.

class ConcertView(View):
    template = 'concertindex.html'

    def get(self, request):
        return render(request, self.template)


class RegisterConcert(View):
    template = 'createconcert.html'

    def get(self, request):
        form = ConcertForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('concert:concertindex'))
        return render(request, self.template, {'form': form})


'''class RegisterSeat(View):
    template = 'seattype.html'

    def get(self, request):
        form = ConcertSeatForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ConcertSeatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('concert:concertindex'))
        return render(request, self.template, {'form': form})'''


class EditConcert(View):
    template = 'editConcert.html'

    def get(self, request):
        form = ConcertForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('concert:concertindex'))
        return render(request, self.template, {'form': form})

