# Generated by Django 3.1.2 on 2021-04-16 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('persons', '0011_auto_20210415_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='country_person', to='places.country', verbose_name='país'),
        ),
    ]
