# Generated by Django 4.2.7 on 2023-11-09 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_workperiod_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workperiod',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 12, 54, 39, 155585), verbose_name='Created on'),
        ),
    ]