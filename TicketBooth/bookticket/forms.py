from django.forms import ModelForm
from django import forms

from registration.models import BookingM, BookingC


class MovieBookingForm(ModelForm):
    bookingID = forms.CharField(widget=forms.NumberInput)
    movieID = forms.CharField(widget=forms.NumberInput)
    numberOfSeats = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = BookingM
        fields = ['bookingID', 'movieID', 'numberOfSeats']


class ConcertBookingForm(ModelForm):
    bookingID = forms.CharField(widget=forms.NumberInput)
    concertID = forms.CharField(widget=forms.NumberInput)
    numberOfSeats = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = BookingC
        fields = ['bookingID', 'concertID', 'numberOfSeats']
