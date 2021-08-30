from django.db import models

class Muffin(models.Model):
    title = models.CharField(max_length=54)
    description = models.TextField()
    image = models.ImageField(upload_to= 'muffin')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Feca de Modificación')

class Meta:
    verbose_name ='Ponquesito'
    verbose_name_plural = 'Panquesitos'

def __str__(self):
     return self.title
