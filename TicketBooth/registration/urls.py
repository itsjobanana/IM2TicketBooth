from . import views
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', views.HomeView.as_view(),name='index'), #127.0.0.1/registration/
    path('createCustomer', views.RegisterUser.as_view(), name='create_customer'),#127.0.0.1/registration/createuser
    path('login',views.Login.as_view(),name='login'),
    path('logout', views.LogOut.as_view(), name='logout'),
    path('editProfile',views.EditProfile.as_view(),name='editProfile'),
    path('concertMovie', views.ChooseView.as_view(), name='concertmovie'),
]
