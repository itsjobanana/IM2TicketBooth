from .import views
from django.urls import path

app_name = 'ticket'

urlpatterns = [
    path('ticketM', views.TicketMView.as_view(), name='ticket_M'),
]