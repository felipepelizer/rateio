# Generated by Django 4.1.7 on 2023-02-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateio_site', '0007_employee_fk_employee_replaced_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_type',
            name='desc_access_type',
            field=models.CharField(max_length=512, null=True, verbose_name='Access Type'),
        ),
    ]
