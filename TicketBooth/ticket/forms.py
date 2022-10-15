from django import forms
from django.forms import ModelForm

from registration.models import TicketC, TicketM, BookingM, BookingC


class TCForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingM.objects.all())
    total = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = TicketC
        fields = ['bookingID', 'total']


class TMForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingC.objects.all())
    total = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = TicketM
        fields = ['bookingID', 'total']