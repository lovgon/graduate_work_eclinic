from django.contrib import admin

from certificates.models import Hospital, CertificateType, Certificate


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass


@admin.register(CertificateType)
class CertificateTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass
