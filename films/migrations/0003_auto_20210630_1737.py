# Generated by Django 2.2.24 on 2021-06-30 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20210630_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmstowatch',
            old_name='Original_name',
            new_name='Originalname',
        ),
    ]
