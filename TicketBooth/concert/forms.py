from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from registration.models import *


class ConcertForm(ModelForm):
    type_seat = (('V', 'VIP'), ('R', 'Regular'))
    concertName = forms.CharField(widget=forms.TextInput)
    artist = forms.CharField(widget=forms.TextInput)
    venue = forms.CharField(widget=forms.TextInput)
    concertDate = forms.DateField(widget=forms.SelectDateWidget)
    timeStart = forms.TimeField(widget=forms.TimeInput)
    seatType = forms.CharField(widget=forms.Select(choices=type_seat))
    price = forms.FloatField(widget=forms.NumberInput)
    capacity = forms.IntegerField(widget=forms.NumberInput)

    def __init__(self, *args, **kwargs):
        super(ConcertForm, self).__init__(*args, **kwargs)
        self.fields['concertName'].label = "Concert Name"
        self.fields['concertDate'].label = "Concert Date"
        self.fields['timeStart'].label = "Time"
        self.fields['seatType'].label = "Seat Type"
        self.fields['concertName'].required = True
        self.fields['artist'].required = True
        self.fields['venue'].required = True
        self.fields['timeStart'].required = True
        self.fields['price'].required = True
        self.fields['capacity'].required = True

    class Meta:
        model = Concert
        fields = ['concertName', 'artist', 'venue', 'concertDate', 'timeStart', 'seatType', 'price', 'capacity']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "This concert was already made.",
            }
        }

class EditConcertForm(ModelForm):
    type_seat = (('V', 'VIP'), ('R', 'Regular'))
    concertName = forms.CharField(widget=forms.TextInput)
    artist = forms.CharField(widget=forms.TextInput)
    venue = forms.CharField(widget=forms.TextInput)
    concertDate = forms.DateField(widget=forms.SelectDateWidget)
    timeStart = forms.TimeField(widget=forms.TimeInput)
    seatType = forms.CharField(widget=forms.Select(choices=type_seat))
    price = forms.FloatField(widget=forms.NumberInput)
    capacity = forms.IntegerField(widget=forms.NumberInput)

    def __init__(self, *args, **kwargs):
        super(EditConcertForm, self).__init__(*args, **kwargs)
        self.fields['concertName'].label = "Concert Name"
        self.fields['concertDate'].label = "Concert Date"
        self.fields['timeStart'].label = "Time"
        self.fields['seatType'].label = "Seat Type"

    class Meta:
        model = Concert
        fields = ['concertName', 'artist', 'venue', 'concertDate', 'timeStart', 'seatType', 'price', 'capacity']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "This concert was already made.",
            }
        }