from django.contrib import admin
from django.urls import path
from profiles_api import views

urlpatterns = [
    path("an_apiview/", views.HelloApiView.as_view()) #The HelloApiView is a rest_framework class that's why you need the .as_view
    
]
