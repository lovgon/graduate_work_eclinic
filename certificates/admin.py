from django.contrib import admin

from certificates.models import Hospital, CertificateType, Certificate


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )


@admin.register(CertificateType)
class CertificateTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'form',
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'certificate_type',
        'hospital',
        'client',
        'created_date',
        'executed_date',
    )

