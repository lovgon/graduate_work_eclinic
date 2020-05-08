# Generated by Django 3.0.5 on 2020-05-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0010_auto_20200507_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='status',
            field=models.CharField(choices=[('in_processing', 'В обработке'), ('confirmed', 'Подтверждено'), ('denied', 'Отклонено')], default='in_processing', max_length=30, verbose_name='Подтверждение'),
        ),
    ]
