from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import User, BookingM, BookingC
from ticket.forms import TMForm, TCForm


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
        return render(request, self.template)


class TicketM(View):
    template = 'ticketM.html'

    def get(self, request):
        form = TMForm()
        form.fields['bookingID'].queryset= BookingM.objects.filter(username_id = request.session['username'])
        #form.fields['total'].queryset
        return render(request,self.template,{'form':form})

    def post(self, request):
        form = TMForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form': form})

class TicketC(View):
    template = 'ticketC.html'

    def get(self, request):
        form = TCForm()
        form.fields['bookingID'].queryset = BookingC.objects.filter(username_id=request.session['username'])
        return render(request,self.template,{'form':form})