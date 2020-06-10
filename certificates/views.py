import datetime

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from certificates.forms import CertificateForm
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
        'processed',
        '-executed_date',
        '-created_date',
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
        'processed',
        '-executed_date',
        '-created_date',
    )

    paginator = Paginator(cert_signature_form, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        # "cert_signature_form": cert_signature_form,
        "cert_signature_form": page,
    }

    return render(request, "account/cert_signature.html", context)


class ApplyView(View):
    def post(self, request, certificate_id):
        print(request.POST)
        if not request.user.is_authenticated:
            raise PermissionError

        hospital = request.user.hospital
        if not hospital:
            raise PermissionError

        doctor = request.user.username

        certificate = Certificate.objects.filter(id=certificate_id, hospital=hospital).first()
        if not certificate:
            raise Http404

        form = certificate.get_form()
        form = form(request.POST)
        form.is_valid()

        certificate.processed = True
        certificate.status = ConfirmChoice.CONFIRMED
        certificate.executed_date = datetime.datetime.now()
        certificate.doctor = doctor
        certificate.additional_fields = form.cleaned_data
        certificate.save()

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
            processed=True,
            status=ConfirmChoice.DENIED,
            executed_date=datetime.datetime.now(),
            doctor=doctor
        )
        return redirect("cert_signature")
