# Generated by Django 3.2.6 on 2021-09-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('names', models.CharField(max_length=50, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('id_patient', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('departament', models.CharField(max_length=50, verbose_name='Departamento')),
                ('city', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('direccion', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dirección')),
                ('rh', models.CharField(choices=[('A+', 'A positivo'), ('A-', 'A negativo'), ('O+', 'O positivo'), ('O-', 'O negativo'), ('AB+', 'AB positivo'), ('AB-', 'AB negativo'), ('B+', 'B positivo'), ('B-', 'B negativo')], default='A+', max_length=3, verbose_name='Tipo de sangre')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo electronico')),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('state', models.CharField(choices=[('Interno', 'Interno'), ('Alta', 'Alta'), ('Recuperación', 'Recuperación'), ('Sano', 'Sano'), ('requiere cirugia', 'requiere cirugia')], default='Sano', max_length=30)),
                ('notas', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'Pacientes',
            },
        ),
    ]
