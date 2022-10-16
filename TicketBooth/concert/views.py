#import cursor as cursor
from django.db import connection

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

class ConcertView(View):
    template = 'concertIndex.html'

    def get(self, request):
        return render(request, self.template)


class RegisterConcert(View):
    template = 'createConcert.html'

    def get(self, request):
        form = ConcertForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('concert:concertIndex'))
        return render(request, self.template, {'form': form})


class DisplayEdit(View):
    template = 'displayEdit.html'

    def get(self, request):
        display = Concert.objects.all()
        return render(request, self.template, {'Concert': display})


class EditConcert(View):
    template = 'editConcert.html'

    def get(self, request, id):
        concert = Concert.objects.get(pk=int(id))
        form = EditConcertForm(instance=concert)
        return render(request, self.template, {'form': form})

    def post(self, request, id):
        concert = Concert.objects.get(pk=int(id))
        form = EditConcertForm(request.POST, instance=concert)
        if form.is_valid:
            form.save()
        return redirect(reverse('index.html'))


class DisplayConcert(View):
    template = 'displayConcert.html'

    def get(self, request):
        display = Concert.objects.all()
        return render(request, self.template, {'Concert': display})


class DeleteConcert(View):
    template = 'editConcert.html'

    def get(self, request, id):
        concert = Concert.objects.get(pk=int(id))
        form = ConcertForm(instance=concert)
        concert.delete()
        return redirect(reverse('concert:displayEdit'))
        return render(request, self.template, {'form': form})

