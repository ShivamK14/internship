from django.urls import path
from . import views

urlpatterns = [
    path('download', views.download),
    path('home', views.home),

]