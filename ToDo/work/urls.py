from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login,name='kt'),
    path('', views.index,name='index'),
    path("logout/", views.logout, name="homepage"),


]
