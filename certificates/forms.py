from django import forms

from certificates.models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = (
            "certificate_type",
            "hospital",
        )

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class Type086(forms.Form):
    past_illnesses = forms.CharField(label='Перенесённые заболевания', max_length=400)
