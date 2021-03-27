from django.contrib import admin
from django.urls import path
from .views import index, bane1, bane2, bane3, bane4 #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
    path('bane1/', bane1, name='bane1'),
    path('bane2/', bane2, name='bane2'),
    path('bane3/', bane3, name='bane3'),
    path('bane4/', bane4, name='bane4'),
]