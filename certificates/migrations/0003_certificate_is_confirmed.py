# Generated by Django 3.0.5 on 2020-05-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("certificates", "0002_auto_20200430_2215"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="status",
            field=models.BooleanField(default=False),
        ),
    ]
