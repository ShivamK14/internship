from django.db import models
from django.contrib.auth.models import User


class Webhook(models.Model):
    deviceId = models.CharField(max_length=30)
    data = models.JSONField(max_length=100, default=False)
    #userId = models.CharField(max_length=30)
    #name = models.CharField(max_length=30)
    #nickname = models.CharField(max_length=30)
    #localDeviceId = models.CharField(max_length=30)
    #errorCode = models.CharField(max_length=30)
    #states = models.CharField(max_length=30)
    #tfa = models.CharField(max_length=30)
