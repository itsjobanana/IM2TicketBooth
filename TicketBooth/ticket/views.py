from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import User, BookingM, Movie
from ticket.forms import TicketMForm


# Create your views here.

class Login(View):
    template = 'ticketLogin.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = User.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('ticket:ticket_index'))
        except User.DoesNotExist:
            user = None

        return render(request, self.template,{'msg':'Incorrect username/ password.'})


class TicketIndex(View):
    template = 'ticketIndex.html'

    def get(self, request):
        form = TicketMForm()
        return render(request, self.template, {'form': form})


class TicketMView(View):
    template = 'ticketM.html'

    def get(self, request):
        form = TicketMForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = TicketMForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect(reverse('ticket:printTicket'))
        return render(request, self.template, {'form': form})


class TicketCView(View):
    template = 'ticketM.html'

    def get(self, request):
        form = TicketMForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = TicketMForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect(reverse('ticket:printTicket'))
        return render(request, self.template, {'form': form})


class CancelM(View):
    template = 'cancelM.html'

    def get(self, request):
        form = TicketMForm()
        return render(request, self.template, {'form': form})


class CancelC(View):
    template = 'cancelC.html'

    def get(self, request):
        form = TicketMForm()
        return render(request, self.template, {'form': form})