import django.db.models.deletion
from django.db import models
from datetime import date


class employed(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombres', null=False)
    lastname = models.CharField(max_length=50, verbose_name='Apellidos', null=False)
    departament = models.CharField(max_length=50, verbose_name='Departamento', null=False)
    city = models.CharField(max_length=30, verbose_name='Ciudad', null=True, blank=True)
    direction = models.CharField(max_length=30, verbose_name='Dirección', null=True, blank=True)
    blood_type = [
        ('A+', 'A positivo'),
        ('A-', 'A negativo'),
        ('O+', 'O positivo'),
        ('O-', 'O negativo'),
        ('AB+', 'AB positivo'),
        ('AB-', 'AB negativo'),
        ('B+', 'B positivo'),
        ('B-', 'B negativo')
    ]
    rh = models.CharField(choices=blood_type, verbose_name='Tipo de sangre', max_length=3, default='A+')
    email = models.CharField(verbose_name='Correo electronico', max_length=50)
    genders = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    gender = models.CharField(choices=genders, default='F',max_length=1)
    charges = [
        ('Secretari@', 'Secretari@'),
        ('Enfermer@', 'Enfermer@'),
        ('Doctor', 'Doctor'),
        ('Cirujano', 'Cirujano'),
        ('Recepcionista', 'Recepcionista'),
        ('Vigilante', 'Vigilante'),
        ('Aseo', 'Aseo')
    ]
    charge = models.CharField(verbose_name='Cargo', choices=charges, default='Recepcionista',  max_length=30)
    schedule = models.DateTimeField()

    def __str__(self):
        return self.names

    def nombreCompleto(self):
        nameComplete= "{0} {1}"
        return nameComplete.format(self.lastname, self.names)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'


class Patients(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombres', null=False)
    lastname = models.CharField(max_length=50, verbose_name='Apellidos', null=False)
    id_patient = models.IntegerField(verbose_name='ID', unique=True, primary_key=True, null=False)
    departament = models.CharField(max_length=50, verbose_name='Departamento', null=False)
    city = models.CharField(max_length=30, verbose_name='Ciudad')
    direccion = models.CharField(max_length=30, verbose_name='Dirección', null=True, blank=True)
    rh = models.CharField(choices=[
        ('A+', 'A positivo'),
        ('A-', 'A negativo'),
        ('O+', 'O positivo'),
        ('O-', 'O negativo'),
        ('AB+', 'AB positivo'),
        ('AB-', 'AB negativo'),
        ('B+', 'B positivo'),
        ('B-', 'B negativo')
    ], verbose_name='Tipo de sangre', max_length=3, default='A+')
    email = models.CharField(verbose_name='Correo electronico', max_length=50, null=True, blank=True)
    gender = models.CharField(choices=[
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ], max_length=1, default='F')
    state = models.CharField(choices=[
        ('Interno', 'Interno'),
        ('Alta', 'Alta'),
        ('Recuperación', 'Recuperación'),
        ('Sano', 'Sano'),
        ('requiere cirugia', 'requiere cirugia' )
    ], max_length=30, default='Sano')
    notas= models.CharField(max_length=1000, null= True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'Pacientes'


class rooms(models.Model):
    n_room = models.CharField(max_length=30, verbose_name='Número de sala', primary_key=True, null=False, blank=False)
    capacity = models.IntegerField(verbose_name='Capacidad de sala')
    funtion = models.CharField(verbose_name='Función de la sala', max_length=30)

    def __str__(self):
        return self.n_room

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        db_table = 'Salas'

class visitors(models.Model):
    ID_visitor = models.CharField(max_length=12, verbose_name='ID visitante', primary_key=True, null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, verbose_name= 'Nombre Visitante')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos visitante')
    city = models.CharField(max_length=50, verbose_name='Ciudad de residencia')
    direction = models.CharField(max_length=60, verbose_name='Dirección de residencia')
    email = models.CharField(max_length=80, verbose_name='Correo Electronico', unique=True)
    relation = models.CharField(max_length=80, verbose_name='Relacion con el interno')
    datevisit = models.DateField()
    id_patient = models.ForeignKey(Patients,on_delete=models.CASCADE)

    def __str__(self):
        return name.self

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'Visitantes'


