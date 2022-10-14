from . import views
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', views.HomeView.as_view(),name='index'), #127.0.0.1/registration/
    path('createCustomer', views.RegisterCustomer.as_view(), name='create_customer'), #127.0.0.1/registration/createuser
    path('login',views.Login.as_view(),name='login'),
    path('logoff', views.LogOff.as_view(), name='logoff'),
    path('editProfile',views.EditProfile.as_view(),name='edit_profile'),
]