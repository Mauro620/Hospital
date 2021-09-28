import django.db.models.deletion
from django.db import models
from datetime import date

class patients(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombres', null=False)
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
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'Pacientes'