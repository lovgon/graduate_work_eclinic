# Generated by Django 3.0.5 on 2020-05-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("certificates", "0006_auto_20200505_1116"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="executed_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выдачи справки"
            ),
        ),
    ]
