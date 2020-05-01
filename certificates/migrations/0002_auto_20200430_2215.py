# Generated by Django 3.0.5 on 2020-04-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'готовую справку', 'verbose_name_plural': 'Готовые справки'},
        ),
        migrations.AlterModelOptions(
            name='certificatetype',
            options={'verbose_name': 'форму справок', 'verbose_name_plural': 'Формы справок'},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name': 'медицинское учереждение', 'verbose_name_plural': 'Медицинские учереждения'},
        ),
        migrations.AddField(
            model_name='certificatetype',
            name='form',
            field=models.CharField(default=0, max_length=128, verbose_name='Форма мед. документа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificatetype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название мед. документа'),
        ),
    ]