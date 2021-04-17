from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers



urlpatterns = [
    path('', views.WebhookView.as_view()),
    path('webhook', views.WebhookRecieveView.as_view()),
    path('list', views.WebhookList.as_view()),
    path('<int:id>', views.WebhookDetailView.as_view()),
]
