# Generated by Django 4.1.7 on 2023-02-21 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rateio_site', '0015_alter_employee_fk_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fk_user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
    ]