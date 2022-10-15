from .import views
from django.urls import path

app_name = 'ticket'

urlpatterns = [
    path('ticketLogin', views.Login.as_view(), name='login'),
    path('ticketIndex', views.TicketIndex.as_view(), name='ticket_index'),
    path('ticketM', views.TicketMView.as_view(), name='ticket_M'),
    path('ticketC', views.TicketCView.as_view(), name='ticket_C'),
    path('cancelC', views.CancelC.as_view(), name='cancel_C'),
    path('cancelM', views.CancelM.as_view(), name='cancel_M'),

]