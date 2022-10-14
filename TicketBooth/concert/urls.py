from . import views
from django.urls import path

app_name = 'concert'


urlpatterns = [
    path('', views.ConcertView.as_view(), name='concertIndex'),
    path('createConcert', views.RegisterConcert.as_view(), name='createConcert'),
    path('editConcert', views.EditConcert.as_view(), name='editConcert'),
]
