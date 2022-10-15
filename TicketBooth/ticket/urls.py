from .import views
from django.urls import path

app_name = 'ticket'

urlpatterns = [
    path('ticketLogin', views.Login.as_view(), name='login'),
    path('ticketIndex', views.TicketIndex.as_view(), name='ticket_index'),
    path('ticketM', views.TicketM.as_view(), name='ticket_M'),
    path('ticketC', views.TicketC.as_view(), name='ticket_C'),

]