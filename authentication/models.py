from django.db import models
from django.contrib.auth.models import User


class UserOTP(models.Model):
    otp = models.IntegerField(default=123456)

