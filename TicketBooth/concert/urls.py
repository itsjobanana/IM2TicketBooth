from . import views
from django.urls import path

app_name = 'concert'


urlpatterns = [
    path('', views.ConcertView.as_view(), name='concertIndex'),
    path('createConcert', views.RegisterConcert.as_view(), name='createConcert'),
    path('displayEdit', views.DisplayEdit.as_view(), name='displayEdit'),
    path('editConcert/<int:id>', views.EditConcert.as_view(), name='editConcert'),
    path('displayConcert', views.DisplayConcert.as_view(), name='displayConcert'),
    path('deleteConcert/<int:id>',views.DeleteConcert.as_view(),name='delete_concert'),
]
