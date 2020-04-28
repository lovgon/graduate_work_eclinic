from django.db import models

from main.models import Account


class Hospital(models.Model):
    name = models.CharField(max_length=2000, verbose_name='Название больницы')
    address = models.CharField(max_length=255, verbose_name='Адрес больницы')

    def __str__(self):
        return self.name


class CertificateType(models.Model):
    name = models.CharField(max_length=120, verbose_name='Форма справки')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    certificate_type = models.ForeignKey(CertificateType, verbose_name='Тип справки', on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, verbose_name='Мед. учереждение', on_delete=models.PROTECT)
    client = models.ForeignKey(Account, verbose_name='Пациент', on_delete=models.PROTECT)
    created_date = models.DateTimeField(verbose_name='Дата подачи заявки', auto_now_add=True)
    executed_date = models.DateTimeField(verbose_name='Дата выдачи справки', auto_now_add=True)

    def __str__(self):
        return f"{self.certificate_type} {self.hospital} {self.client} {self.created_date} {self.executed_date}"
