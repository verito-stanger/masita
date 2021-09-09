from django.db.models import Model, CharField,TextField, ImageField, DateTimeField 

class Muffin(Model):
    title = CharField(max_length=54)
    description =TextField()
    image = ImageField(upload_to= 'muffin')
    created =DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated= DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

class Meta:
    verbose_name ='Ponquesito'
    verbose_name_plural = 'Panquesitos'

def __str__(self):
     return self.title
