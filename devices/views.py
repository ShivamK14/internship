import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from .models import FileAdmin


# Create your views here.


def home(request):
    context = {'file': FileAdmin.objects.all()}
    return HttpResponse(request, context)


def download(request, path):
    file_path = os.path.join(settings.Media_root.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type='application/adminupload')
            response['Content-Disposition'] = 'inline;filename' + os.path.basename(file_path)
            return response
    raise Http404
