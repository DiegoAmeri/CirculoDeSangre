# Generated by Django 3.1.2 on 2021-04-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0012_person_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='relation',
            field=models.CharField(choices=[('Student', 'Estudiante'), ('Teacher', 'Docente'), ('NonTeaching', 'No Docente'), ('Community', 'Comunidad')], default='Student', max_length=15, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_type',
            field=models.CharField(choices=[('Assistant', 'Asistente'), ('Speaker', 'Ponente'), ('Collaborator', 'Colaborador'), ('Organizer', 'Organizador'), ('Evaluator', 'Evaluador')], default='Assistant', max_length=15, verbose_name='tipo'),
        ),
    ]
