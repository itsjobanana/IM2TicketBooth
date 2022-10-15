from django import forms
from django.forms import ModelForm

from registration.models import TicketC, TicketM


class TCForm(ModelForm):
    bookingID = forms.ModelChoiceField(widget=forms.Select(), queryset=None)
    total = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = TicketC
        fields = ['bookingID', 'total']


class TMForm(ModelForm):
    bookingID = forms.ModelChoiceField(widget=forms.Select(), queryset=None)
    total = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = TicketM
        fields = ['bookingID', 'total']