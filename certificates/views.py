from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView, TemplateView, ListView

from certificates.models import Certificate


class CreateCertificate(CreateView):
    model = Certificate

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404

        Certificate.objects.create()
