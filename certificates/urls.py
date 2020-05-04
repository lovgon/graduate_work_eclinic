from django.urls import path

from certificates.views import cert_order, cert_signature

urlpatterns = [
    path('cert_order/', cert_order, name='cert_order'),
    path('cert_signature/', cert_signature, name='cert_signature'),
]
