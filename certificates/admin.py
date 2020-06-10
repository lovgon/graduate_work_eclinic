from django.contrib import admin

from certificates.models import Hospital, CertificateType, Certificate, ConfirmChoice


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
    )


@admin.register(CertificateType)
class CertificateTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "form",
        "short_name",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "certificate_type",
        "hospital",
        "client",
        "created_date",
        "executed_date",
        "status",
        "additional_fields",
    )
