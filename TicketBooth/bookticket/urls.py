from . import views
from django.urls import path

app_name = 'bookticket'

urlpatterns = [
    path('', views.HomeBookTicket.as_view(), name='bookTicket_Index'),  # 127.0.0.1/bookticket
    path('bookMovie', views.MovieBookingTicket.as_view(), name='movie_Ticket'),  # 127.0.0.1/bookMovie
    path('bookConcert', views.ConcertBookingTicket.as_view(), name='concert_Ticket'),  # 127.0.0.1/bookConcert
    path('displayBooking', views.DisplayBooking.as_view(), name='display_Booking'),
    ]
