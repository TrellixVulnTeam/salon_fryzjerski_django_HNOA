# Generated by Django 4.0.1 on 2022-01-18 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fryzjer', '0006_rename_service_visit_servicee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='Servicee',
        ),
        migrations.AddField(
            model_name='visit',
            name='servicee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='serwis', to='fryzjer.servicee'),
        ),
    ]
