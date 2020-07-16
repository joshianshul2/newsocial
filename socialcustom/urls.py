
from django.urls import path
from . import  views

urlpatterns = [
    path("",views.signup,name="aj"),
    path("index", views.index, name='index.html'),
    path("login", views.login, name='login.html'),


]