from django.urls import path

from . import views

urlpatterns = [

    path('', views.coordinates, name='coordinates'),
   
   
]