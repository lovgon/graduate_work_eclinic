from django.urls import path

from certificates.views import cert_order, cert_signature, ApplyView, DeniView

urlpatterns = [
    path("cert_order/", cert_order, name="cert_order"),
    path("cert_signature/", cert_signature, name="cert_signature"),
    path("cert_signature/apply/<int:certificate_id>", ApplyView.as_view(), name="cert_apply"),
    path("cert_signature/deni/<int:certificate_id>", DeniView.as_view(), name="cert_deni"),
]
