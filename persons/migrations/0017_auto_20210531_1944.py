# Generated by Django 3.1.2 on 2021-05-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0016_auto_20210423_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='affiliation',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Filiación'),
        ),
    ]
