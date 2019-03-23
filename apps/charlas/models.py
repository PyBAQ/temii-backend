# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class CharlaModel(models.Model):

    ESTADO_POSIBLE = 'posible'
    ESTADO_AGENDADO = 'agendado'
    ESTAOO_FINALIZADO = 'finalizado'

    ESTADO_CHOICES = (
       (ESTADO_POSIBLE, 'Temas Posibles'),
       (ESTADO_AGENDADO, 'Temas agendados'),
       (ESTAOO_FINALIZADO, 'Temas finalizados'),
    )

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField("CategoriaModel")
    prerequisitos = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES, default="posible")
    fecha_taller = models.DateField(blank=True, null=True)
    votos = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(User, related_name='propone_charla')
    tallerista = models.ForeignKey(User, related_name='tallerista',
                                   blank=True, null=True)
    talleriast_no_usuario = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['votos']

    def __str__(self):
        return self.titulo


class UsuarioVotoModel(models.Model):
    usuario = models.ForeignKey(User)
    charla = models.ForeignKey("CharlaModel")
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'charla')
