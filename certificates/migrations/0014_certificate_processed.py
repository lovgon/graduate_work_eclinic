# Generated by Django 3.0.6 on 2020-05-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0013_auto_20200508_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='processed',
            field=models.BooleanField(default=False, verbose_name='Обработанно'),
        ),
    ]
