# Generated by Django 4.0.5 on 2023-07-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='serial_motor',
            field=models.CharField(max_length=50),
        ),
    ]