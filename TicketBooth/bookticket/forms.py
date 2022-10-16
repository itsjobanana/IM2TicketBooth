from datetime import date
from django.forms import ModelForm
from django import forms

from registration.models import BookingM, BookingC, Concert, Movie

type_room = (('V', 'VIP'), ('R', 'Regular'))
type_seat = (('V', 'VIP'), ('R', 'Regular'))


class MovieBookingForm(ModelForm):
    movieID = forms.ModelChoiceField(widget=forms.Select(), queryset=Movie.objects.only('movieID'))
    status = False
    numberOfSeats = forms.IntegerField(widget=forms.NumberInput)
    roomType = forms.CharField(widget=forms.Select(choices=type_room))

    def __int__(self, *args, **kwargs):
        super(MovieBookingForm, self).__init__(*args, **kwargs)
        self.instance.status = self.status

    class Meta:
        model = BookingM
        fields = ['movieID', 'numberOfSeats', 'roomType']


class ConcertBookingForm(ModelForm):
    concertID = forms.ModelChoiceField(widget=forms.Select(), queryset=Concert.objects.only('concertID'))
    status = False
    numberOfSeats = forms.IntegerField(widget=forms.NumberInput)
    seatType = forms.CharField(widget=forms.Select(choices=type_seat))

    def __int__(self, *args, **kwargs):
        super(ConcertBookingForm, self).__init__(*args, **kwargs)
        self.instance.status = self.status

    class Meta:
        model = BookingC
        fields = ['concertID', 'numberOfSeats', 'seatType']
