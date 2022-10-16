from django.db import connection
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from .forms import CustomerForm, AdminForm
from .models import User, Admin, Customer


# Create your views here.
class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class RegisterCustomer(View):
    template = 'createCustomer.html'

    def get(self, request):
        form = CustomerForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})


class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = User.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('registration:index'))
        except User.DoesNotExist:
            user = None

        return render(request, self.template,{'msg':'Incorrect username/ password.'})

class LogOut(View):
    def get(self, request):
        try:
            del request.session['username']
            del request.session['type']
        except:
            pass
        return redirect(reverse('registration:index'))


class EditProfile(View):
    template = 'editProfile.html'

    def get(self, request):
            if request.session['type'] == 'U':
                customer = Customer.objects.get(pk=request.session['username'])
                form = CustomerForm(instance=customer)

            else:
                admin = Admin.objects.get(pk=request.session['username'])
                form = AdminForm(instance=admin)
            return render(request, self.template,{'form':form})

    def post(self,request):
        if request.session['type'] == 'U':
            customer = Customer.objects.get(pk=request.session['username'])
            form = CustomerForm(request.POST,instance=customer)
        else:
            admin = Admin.objects.get(pk=request.session['username'])
            form = AdminForm(request.POST,instance=admin)
        if form.is_valid:
            form.save()
        return render(request, 'index.html')


class ChooseView(View):
    template = 'concertmovie.html'

    def get(self, request):
        return render(request, self.template)