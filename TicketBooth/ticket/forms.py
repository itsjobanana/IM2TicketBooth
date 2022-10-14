from django import forms
from django.forms import ModelForm

from registration.models import BookingM, TicketM


class TicketMForm(ModelForm):
    bookingID = forms.ModelChoiceField(queryset=BookingM.objects.all())
    total = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = TicketM
        fields = ['bookingID','total']