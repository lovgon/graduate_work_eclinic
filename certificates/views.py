import datetime

from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from certificates.forms import CertificateForm, Type086
from certificates.models import Certificate, ConfirmChoice


class CreateCertificate(CreateView):
    model = Certificate

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404

        Certificate.objects.create()


def cert_order(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        certificate_form = CertificateForm(request.POST)
        if certificate_form.is_valid():
            cert = certificate_form.save(commit=False)
            cert.client = request.user
            cert.created_date = timezone.now()
            cert.save()
    else:
        certificate_form = CertificateForm()

    filed_certificates = Certificate.objects.order_by(
        'status',
        '-executed_date',
        '-created_date'
    )

    context = {
        "certificate_form": certificate_form,
        "filed_certificates": filed_certificates,
    }

    return render(request, "account/cert_order.html", context)


def cert_signature(request):
    if not request.user.is_authenticated:
        return redirect("login")

    hospital = request.user.hospital
    if not hospital:
        return redirect("cert_order")

    cert_signature_form = Certificate.objects.filter(hospital=request.user.hospital).order_by(
        'status',
        '-executed_date',
        '-created_date'
    )

    context = {
        "cert_signature_form": cert_signature_form,
        'cert_types_form': {
            '086/у': Type086
        }
    }

    return render(request, "account/cert_signature.html", context)


class ApplyView(View):
    def get(self, request, certificate_id):
        if not request.user.is_authenticated:
            raise PermissionError

        hospital = request.user.hospital
        if not hospital:
            raise PermissionError

        doctor = request.user.username

        Certificate.objects.filter(id=certificate_id, hospital=hospital).update(
            status=ConfirmChoice.CONFIRMED,
            executed_date=datetime.datetime.now(),
            doctor=doctor
        )
        return redirect("cert_signature")


class DeniView(View):
    def get(self, request, certificate_id):
        if not request.user.is_authenticated:
            raise PermissionError

        hospital = request.user.hospital
        if not hospital:
            raise PermissionError

        doctor = request.user.username

        Certificate.objects.filter(id=certificate_id, hospital=hospital).update(
            status=ConfirmChoice.DENIED,
            executed_date=datetime.datetime.now(),
            doctor=doctor
        )
        return redirect("cert_signature")
