# Generated by Django 4.0.5 on 2022-06-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
            ],
            options={
                'verbose_name_plural': 'Familiares',
            },
        ),
    ]
