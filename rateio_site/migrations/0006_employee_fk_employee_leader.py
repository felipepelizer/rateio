# Generated by Django 4.1.7 on 2023-02-21 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rateio_site', '0005_access_type_city_contract_type_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fk_employee_leader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='rateio_site.employee', verbose_name='Leader'),
        ),
    ]
