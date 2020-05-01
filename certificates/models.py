from django.db import models

from main.models import Account


class Hospital(models.Model):
    name = models.CharField(max_length=2000, verbose_name='Название больницы')
    address = models.CharField(max_length=255, verbose_name='Адрес больницы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'медицинское учереждение'
        verbose_name_plural = 'Медицинские учереждения'


class CertificateType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название мед. документа')
    form = models.CharField(max_length=128, verbose_name='Форма мед. документа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'форму справок'
        verbose_name_plural = 'Формы справок'


class Certificate(models.Model):
    certificate_type = models.ForeignKey(CertificateType, verbose_name='Тип справки', on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, verbose_name='Мед. учереждение', on_delete=models.PROTECT)
    client = models.ForeignKey(Account, verbose_name='Пациент', on_delete=models.PROTECT)
    created_date = models.DateTimeField(verbose_name='Дата подачи заявки', auto_now_add=True)
    executed_date = models.DateTimeField(verbose_name='Дата выдачи справки', auto_now_add=True)

    def __str__(self):
        return f"{self.certificate_type} {self.hospital} {self.client}"

    class Meta:
        verbose_name = 'готовую справку'
        verbose_name_plural = 'Готовые справки'
