from django import forms

from certificates.models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_type']
