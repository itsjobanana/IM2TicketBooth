from django import forms
from django.forms import ModelForm

from registration.models import BookingM, TicketM, Movie, TicketC


class TicketMForm(ModelForm):
    bookingID = forms.ModelChoiceField(widget=forms.Select(), queryset=None)
    total = forms.CharField(widget=forms.NumberInput)
    status = True

    class Meta:
        model = TicketM
        fields = ['bookingID', 'total']


class TicketCForm(ModelForm):
    bookingID = forms.ModelChoiceField(widget=forms.Select(), queryset=None)
    total = forms.CharField(widget=forms.NumberInput)
    status = True

    class Meta:
        model = TicketC
        fields = ['bookingID', 'total']