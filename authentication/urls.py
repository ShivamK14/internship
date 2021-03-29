from django.urls import path
from . import views

urlpatterns = [
    path('register', views.Register.as_view()),
    path('login', views.LoginView.as_view()),
    path('otp', views.VerifyOTPView.as_view())
]