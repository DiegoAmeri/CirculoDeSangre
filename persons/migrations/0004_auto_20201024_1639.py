# Generated by Django 3.1.2 on 2020-10-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20201023_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email address'),
        ),
    ]
