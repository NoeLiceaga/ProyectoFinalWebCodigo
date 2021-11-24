from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.


class CategoriasTrabajo(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    logo = models.ImageField(upload_to="media/", null=False)
    direccion = models.CharField(max_length=300, null=True)
    telefono = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=500, null=True)
    categoria_principal = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre


class Perfiles(models.Model):
    nivel = models.CharField(max_length=20)

    def __str__(self):
        return self.nivel


class TipoDeTrabajo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class OfertaDeEmpleo(models.Model):
    estados = (('1', 'ACTIVA'), ('2', 'COMPLETA'))
    titulo = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoDeTrabajo, on_delete=CASCADE)
    salario_minimo = models.IntegerField(null=False)
    salario_maximo = models.IntegerField(null=False)
    experiencia = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriasTrabajo, on_delete=CASCADE)
    genero = models.ForeignKey(Genero, on_delete=CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    descripcion = models.CharField(max_length=1000, default="any")
    estado = models.CharField(max_length=15, choices=estados, default=1)
    reclutador = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        txt = "{0} {1}: {2}"
        return txt.format(self.titulo, self.categoria, self.tipo)


class CV(models.Model):
    idiomas = (('1', "Inglés"), ('2', "Chino"),
               ('3', "Aleman"), ('4', "Japones"))
    generos = (('1', 'Cualquiera'), ('2', 'Masculino'), ('3', 'Femenino'))
    id_usuario = models.ForeignKey(User, on_delete=CASCADE, null=True)
    sexo = models.ForeignKey(Genero, on_delete=CASCADE, default=1)
    descripcion = models.CharField(
        max_length=500, null=True)
    profesion = models.CharField(max_length=100, null=True)
    foto = models.ImageField('imagen', upload_to="candidatos/", null=True)
    universidad_nombre = models.CharField(max_length=50, null=True)
    universidad_inicio = models.DateField(null=True)
    universidad_fin = models.DateField(null=True)
    grado = models.CharField(max_length=100, null=True)
    bachiller_nombre = models.CharField(max_length=50)
    bachiller_inicio = models.DateField(null=True)
    bachiller_fin = models.DateField(null=True)

    empleo_anterior_empresa = models.CharField(
        max_length=50, default="Empresa")
    empleo_anterior_puesto = models.CharField(max_length=50)
    empleo_anterior_inicio = models.DateField('Inicio', null=True)
    empleo_anterior_fin = models.DateField('Fin', null=True)

    empleo_anterior2_empresa = models.CharField(
        max_length=50, default="Empresa")
    empleo_anterior2_puesto = models.CharField(max_length=50, null=True)
    empleo_anterior2_inicio = models.DateField(null=True,)
    empleo_anterior2_fin = models.DateField(null=True)
    idioma_extra = models.CharField(
        choices=idiomas, default="Inglés", max_length=20)
    idoma_porcentaje = models.IntegerField(null=True)


class Postulante(models.Model):
    estados = (('1', 'ACEPTADO'), ('2', 'RECHAZADO'), ('3', 'EN PROCESO'))
    oferta = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20)
    estado = models.CharField(max_length=15, choices=estados, default=3)

    def __str__(self):
        txt = "{0}-> {1}: {2}"
        return txt.format(self.oferta, self.usuario, self.estado)


class Estado(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class PruebaPostulante(models.Model):
    oferta = models.ForeignKey(OfertaDeEmpleo, on_delete=CASCADE)
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    estado = models.ForeignKey(Estado, on_delete=CASCADE, default=3)

    def __str__(self):
        txt = "{0}-> {1}: {2}"
        return txt.format(self.oferta, self.usuario, self.estado)
