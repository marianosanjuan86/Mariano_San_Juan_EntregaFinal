from django.db import models
from django.db.models.enums import Choices

class Banda(models.Model):
    nombre = models.CharField(max_length=25)
    estilo = models.CharField(max_length=25)
    fecha_formacion = models.DateField()
    residencia = models.CharField(max_length=25)
    integrantes = models.TextField(blank=True)
    presentacion = models.TextField()
    historia = models.TextField(blank=True)
    discos = models.TextField(blank=True)
    foto = models.ImageField(upload_to= "bandas/fotos" ,blank=True)
    tema_presentacion = models.URLField(blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    youtube = models.URLField(blank=True)
    spotify = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    otro = models.URLField(blank=True)

    def __str__(self): 
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Bandas"

class Noticia(models.Model):
    fecha_alta = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=25)
    noticia = models.TextField()
    foto = models.ImageField(upload_to= "noticias/fotos")
    link = models.URLField(blank=True)

    def __str__(self): 
        return f"{self.titulo}"
    class Meta:
        verbose_name_plural = "Noticias"

class Evento(models.Model) :
    fecha_alta = models.DateTimeField(auto_now_add=True)
    banda = models.CharField(max_length=25)
    fecha_evento = models.DateField()
    horario = models.TimeField()
    lugar = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    comentario = models.TextField(blank=True)
    link_entrada = models.URLField(blank=True)
    link_banda = models.URLField(blank=True)

    def __str__(self): 
        return f"{self.banda} - {self.fecha_evento}"
    class Meta:
        verbose_name_plural = "eventos"
    