# Generated by Django 3.1.2 on 2021-04-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0009_auto_20201028_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user_type',
            field=models.CharField(choices=[('Subscriber', 'Suscriptor'), ('Lecturer', 'Disertante'), ('Collaborator', 'Colaborador'), ('Organizer', 'Organizador'), ('Evaluator', 'Evaluador')], default='Subscriber', max_length=15, verbose_name='tipo'),
        ),
    ]
