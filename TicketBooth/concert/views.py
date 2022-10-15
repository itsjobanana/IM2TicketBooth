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


class DisplayEdit(View):
    template = 'displayEdit.html'

    def get(self, request):
            display = Concert.objects.all()
            return render(request, self.template, {'Concert': display})


class EditConcert(View):
    template = 'editConcert.html'

    def get(self, request, concertID):
        getdata = Concert.objects.get(concertID=concertID)
        form = ConcertForm(instance=getdata)
        return render(request, self.template, {'Concert': form})


class DisplayConcert(View):
    template = 'displayConcert.html'

    def get(self, request):
        display = Concert.objects.all()
        return render(request, self.template, {'Concert': display})


class DeleteConcert(View):
    template = 'editConcert.html'

    def delete(self, request, concertID):
        delete = Concert.objects.get(concertID=concertID)
        delete.delete()
        display = Concert.objects.all()
        return render(request, self.template, {'Concert': display})
