# Generated by Django 3.2.6 on 2021-09-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('departament', models.CharField(max_length=50, verbose_name='Departamento')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ciudad')),
                ('direction', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dirección')),
                ('rh', models.CharField(choices=[('A+', 'A positivo'), ('A-', 'A negativo'), ('O+', 'O positivo'), ('O-', 'O negativo'), ('AB+', 'AB positivo'), ('AB-', 'AB negativo'), ('B+', 'B positivo'), ('B-', 'B negativo')], default='A+', max_length=3, verbose_name='Tipo de sangre')),
                ('email', models.CharField(max_length=50, verbose_name='Correo electronico')),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('charge', models.CharField(choices=[('Secretari@', 'Secretari@'), ('Enfermer@', 'Enfermer@'), ('Doctor', 'Doctor'), ('Cirujano', 'Cirujano'), ('Recepcionista', 'Recepcionista'), ('Vigilante', 'Vigilante'), ('Aseo', 'Aseo')], default='Recepcionista', max_length=30, verbose_name='Cargo')),
                ('schedule', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleados',
            },
        ),
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
                ('state', models.CharField(choices=[('Interno', 'Interno'), ('Alta', 'Alta'), ('Recuperación', 'Recuperación'), ('Sano', 'Sano')], default='Sano', max_length=30)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('n_room', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número de sala')),
                ('capacity', models.IntegerField(verbose_name='Capacidad de sala')),
                ('funtion', models.CharField(max_length=30, verbose_name='Función de la sala')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'db_table': 'Salas',
            },
        ),
    ]
