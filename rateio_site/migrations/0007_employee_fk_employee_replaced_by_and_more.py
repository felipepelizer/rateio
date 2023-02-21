# Generated by Django 4.1.7 on 2023-02-21 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rateio_site', '0006_employee_fk_employee_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fk_employee_replaced_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='replaced_by', to='rateio_site.employee', verbose_name='Replaced By'),
        ),
        migrations.AddField(
            model_name='employee',
            name='fk_employee_replacing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='replacing', to='rateio_site.employee', verbose_name='Replacing'),
        ),
    ]
