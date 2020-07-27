from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('assignwork/<int:getdata_id>/',views.assignment,name='assignwork'),
    path('showinterest/',views.interest,name="showinterest"),
]
