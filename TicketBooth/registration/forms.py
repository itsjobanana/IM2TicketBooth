from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import *


class CustomerForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    type = 'T'


    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['username'].required = False

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['password'].required = False

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['type'].required = True

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['firstname'].required = True

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middleName'].required = False

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['lastname'].required = True

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['address'].required = True

    def clean_password(self):
        password = self.data.get('password')
        if len(password) < 8:
            raise ValidationError('Minimum number of characters for password is 8.')
        else:
            return password


    class Meta:
        model = Customer
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname','address', 'type']

class AdminForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    middlename = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    type = 'A'


    class Meta:
        model = Admin
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname']



