from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView, TemplateView, ListView

from certificates.forms import CertificateForm
from certificates.models import Certificate


class CreateCertificate(CreateView):
    model = Certificate

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404

        Certificate.objects.create()


def cert_order(request):
    if request.method == 'POST':
        certificate_form = CertificateForm(request.POST)
        if certificate_form.is_valid():
            cert = certificate_form.save(commit=False)
            cert.client = request.user
            cert.created_date = timezone.now()
            cert.executed_date = 0
            cert.save()
    else:
        certificate_form = CertificateForm()

    context = {
        'certificate_form': certificate_form,
    }

    return render(request, 'account/cert_order.html', context)


def cert_signature(request):
    cert_signature_form = Certificate.objects.filter(hospital=request.user.hospital)

    context = {
        'cert_signature_form': cert_signature_form,
    }

    return render(request, 'account/cert_signature.html', context)
