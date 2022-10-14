from . import views
from django.urls import path

app_name = 'concert'


urlpatterns = [
    path('', views.ConcertView.as_view(),name='concertindex'),
    path('createconcert', views.RegisterConcert.as_view(),name='createconcert'),
    path('editConcert', views.EditConcert.as_view(), name='editconcert'),
]
