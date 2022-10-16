from django import forms
from django.forms import ModelForm

from registration.models import TicketC, TicketM, BookingM, BookingC, Movie


class TMForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingM.objects.all())
    status = False

    class Meta:
        model = TicketM
        fields = ['bookingID', 'status']


class TCForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingC.objects.all())
    status = False

    class Meta:
        model = TicketC
        fields = ['bookingID', 'status']