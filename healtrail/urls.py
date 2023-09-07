from django.contrib import admin
from django.urls import path
from healtrail import views

urlpatterns = [
    
    path('', views.index, name='healtrail'),
    path('gym-software', views.service, name='service'),
    path('yoga-software', views.yogas, name='yogas'),
    path('doctor-software', views.doctor, name='doctor'),
]
