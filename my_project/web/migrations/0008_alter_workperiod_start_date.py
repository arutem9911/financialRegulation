# Generated by Django 4.2.7 on 2023-11-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_workperiod_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workperiod',
            name='start_date',
            field=models.DateTimeField(verbose_name='Created on'),
        ),
    ]