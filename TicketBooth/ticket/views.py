from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from TicketBooth.ticket.forms import TicketMForm


# Create your views here.


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

