
from django import forms
from django.forms import ModelForm

from registration.models import *

class ConcertForm(ModelForm):
    type_seat = (('V', 'VIP'), ('R', 'Regular'))
    title = forms.CharField(widget=forms.TextInput)
    venue = forms.CharField(widget=forms.TextInput)
    concertDate = forms.DateField(widget=forms.DateInput)
    timeStart = forms.TimeField(widget=forms.TimeInput)
    seatType = forms.CharField(widget=forms.Select(choices=type_seat))
    price = forms.FloatField(widget=forms.NumberInput)
    capacity = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Concert
        fields = ['title', 'venue', 'concertDate', 'timeStart', 'seatType', 'price', 'capacity']


'''class ConcertSeatForm(ModelForm):
    type_seat = (('V', 'VIP'), ('R', 'Regular'))
    seatType = forms.CharField(widget=forms.Select(choices=type_seat))
    price = forms.FloatField(widget=forms.NumberInput)
    capacity = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = ConcertSeat
        fields =['seatType', 'price', 'capacity']'''
