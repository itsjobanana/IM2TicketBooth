from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from registration.models import Movie

type_room = (('V', 'VIP'), ('R', 'Regular'))
room_num = (('1', 'Room1'), ('2', 'Room2'), ('3', 'Room3'), ('4', 'Room4'), ('5', 'Room5'))
price_choice = ('500', '500'), ('1000', '1000')


class MovieForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    roomNum = forms.CharField(widget=forms.Select(choices=room_num))
    dateAvailable = forms.DateField(widget=forms.SelectDateWidget)
    timeAired = forms.TimeField(widget=forms.TimeInput)
    roomType = forms.CharField(widget=forms.Select(choices=type_room))
    price = forms.IntegerField(widget=forms.Select(choices=price_choice))
    capacity = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Movie
        fields = ['title', 'roomNum', 'dateAvailable', 'timeAired', 'roomType', 'price', 'capacity']

