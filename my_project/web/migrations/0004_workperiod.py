# Generated by Django 4.2.7 on 2023-11-09 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_executive_delete_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('end_date', models.DateTimeField(default=None, null=True, verbose_name='Created on')),
                ('executive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_periods', to='web.executive', verbose_name='executive')),
            ],
            options={
                'verbose_name': 'work period',
                'verbose_name_plural': 'work periods',
            },
        ),
    ]