
from django.urls import path
from MyWeatherApp import views  
urlpatterns = [   
    path('', views.home, name = 'home')  
]