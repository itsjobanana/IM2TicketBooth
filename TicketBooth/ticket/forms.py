from django import forms
from django.forms import ModelForm

from registration.models import TicketC, TicketM, BookingM, BookingC


class TMForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingM.objects.all())
    total = forms.ChoiceField()
    status = False

    class Meta:
        model = TicketM
        fields = ['bookingID','total', 'status']


class TCForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingC.objects.all())
    total = forms.CharField(widget=forms.NumberInput)
    status = False

    class Meta:
        model = TicketC
        fields = ['bookingID', 'total', 'status']