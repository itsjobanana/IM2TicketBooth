from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from bookticket.forms import ConcertBookingForm, MovieBookingForm
from registration.models import Concert, Customer, Movie


# Create your views here.

class HomeBookTicket(View):
    template = 'bookTicket_Index.html'

    def get(self, request):
        return render(request, self.template)


class MovieBookingTicket(View):
    template = 'bookTicket_Movie.html'

    def get(self, request):
        allMovie = Movie.objects.all()
        form = MovieBookingForm()
        return render(request, self.template, {'movie': allMovie, 'form': form})

    def post(self, request):
        errorMsg = ''
        form = MovieBookingForm(request.POST)
        allMovie = Movie.objects.all()
        bookingID = request.POST['movieID']
        print('MovieID: ' + bookingID)
        numberOfAttendees = Movie.objects.filter(bookingm__movieID=bookingID).count()
        movie = Movie.objects.get(pk=bookingID)
        print('Number of Attendees: ' + str(numberOfAttendees))
        if numberOfAttendees < movie.capacity:
            customer = Customer.objects.get(pk=request.session['username'])
            attendMovie = form.save(commit=False)
            attendMovie.movieUser = customer
            form.save()
        else:
            errorMsg = 'Movie is already full!'

        return render(request, self.template, {'movies': allMovie, 'form': form, 'errorMsg': errorMsg})


class ConcertBookingTicket(View):
    template = 'bookTicket_Concert.html'

    def get(self, request):
        allConcert = Concert.objects.all()
        form = ConcertBookingForm()
        return render(request, self.template, {'form': form, 'concert': allConcert})

    def post(self, request):
        errorMsg = ''
        form = ConcertBookingForm(request.POST)
        allConcert = Concert.objects.all()
        bookingID = request.POST['concertID']
        print('ConcertID: ' + bookingID)
        numberOfAttendees = Concert.objects.filter(bookingc__concertID=bookingID).count()
        concert = Concert.objects.get(pk=bookingID)
        print('Number of Attendees: ' + str(numberOfAttendees))
        if numberOfAttendees < concert.capacity:
            customer = Customer.objects.get(pk=request.session['username'])
            attendConcert = form.save(commit=False)
            attendConcert.concertUser = customer
            form.save()
        else:
            errorMsg = 'Concert is already full!'

        return render(request, self.template, {'form': form, 'errorMsg': errorMsg, 'concerts': allConcert})


class DisplayBooking(View):
    template = 'displayBooking.html'

    def get(self, request):
        cursorConcert = connection.cursor()
        cursorConcert.callproc('ticketbooth.displayConcertEvent', [request.session['username']])
        displayConcert =cursorConcert.fetchall()
        cursorConcert.close()

        form = ConcertBookingForm()
        return render(request, self.template, {'concert': displayConcert, 'form':form})