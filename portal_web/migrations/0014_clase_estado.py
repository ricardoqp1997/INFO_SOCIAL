# Generated by Django 3.1.3 on 2020-11-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_web', '0013_auto_20201124_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='estado',
            field=models.BooleanField(choices=[(True, 'Clase inactiva'), (False, 'Clase activa')], default=False, verbose_name='Estado de la clase'),
        ),
    ]