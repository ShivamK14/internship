import json
from rest_framework import generics, response, status, request, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Webhook
from .serializers import WebhookSerializer
import requests


class WebhookView(generics.GenericAPIView):

    def post(self, request):
        webhook_url = 'http://127.0.0.1:8000/api/webhooks/webhook'
        data = {'deviceId': 'ShivamK14',
                'data': 'shivamkarle'}
        r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return response.Response('sent')


class WebhookRecieveView(generics.GenericAPIView):
    serializer_class = WebhookSerializer

    def post(self, request):
        webhookurl = 'https://webhook.site/b44cec93-3b21-404b-96bc-e0f8e9bd3069'
        jsondata = request.body
        data = json.loads(jsondata)
        print(data)
        r = requests.post(webhookurl, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        u = Webhook(**data)
        print(u)
        u.save()
        #print(u)
        return response.Response(status=status.HTTP_200_OK)


class WebhookList(generics.ListAPIView):
    serializer_class = WebhookSerializer
   #permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Webhook.objects.all


class WebhookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = WebhookSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Webhook.objects.filter(id=self.request.user)