# Generated by Django 4.1.7 on 2023-02-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateio_site', '0010_remove_employee_fk_employee_leader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_termination',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Termination Date'),
        ),
    ]
