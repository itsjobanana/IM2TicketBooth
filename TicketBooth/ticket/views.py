from django.shortcuts import render
from django.views import View


# Create your views here.


class TicketMView(View):
    template = 'ticketM.html'