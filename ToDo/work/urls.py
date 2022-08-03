from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('kt/', views.kuchtoh,name='kt'),
    path('', views.index,name='index'),
    path("homepage/", views.homepage, name="homepage"),


]
