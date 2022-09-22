# Generated by Django 4.1.1 on 2022-09-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_personal', '0009_sueldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sueldo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='infoacademica',
            name='institucion',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]