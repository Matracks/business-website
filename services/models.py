from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
def custom_upload_to(instance, filename):
    try:
        old_instance = Service.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'services/' + filename
    except ObjectDoesNotExist:
        return 'services/' + filename


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to=custom_upload_to)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
