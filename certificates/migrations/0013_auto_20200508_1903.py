# Generated by Django 3.0.6 on 2020-05-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0012_certificate_additional_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetype',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='Название мед. документа'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=400, verbose_name='Адрес больницы'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='Название больницы'),
        ),
    ]
