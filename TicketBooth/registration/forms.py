from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Customer, Admin, User



class CustomerForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    type = 'U'


    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required = False


    class Meta:
        model = Customer
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname','address']


class AdminForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    middlename = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    type = 'A'
    age = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Admin
        fields = ['password', 'firstname', 'middlename', 'lastname', 'age']