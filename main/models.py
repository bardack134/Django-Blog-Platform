from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    #La línea unique=True se aplica al campo title. Esto significa que cada valor en el campo title debe ser único en toda la tabla de la base de datos. No puede haber dos filas con el mismo valor en el campo title.
    titulo = models.CharField(max_length=200, blank=True, null=True, unique=True) 
    
    #Auto-generación: El campo slug se utiliza para almacenar una versión "amigable" del título que puede ser utilizada en la URL. Este campo se auto-genera a partir del título, y su propósito es crear una URL legible y SEO-friendly.
    slug = models.SlugField(max_length=200, unique=True)
    
    # Este campo se utilizará para almacenar textos más largos, sin una longitud máxima predefinida.
    description = models.TextField(blank=True, null=True)
    
    # Este campo se utilizará para almacenar fechas y horas. 'auto_now_add=True' establece la fecha automáticamente al agregar un nuevo registro.
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
        
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #rdering = ['-created_on'] significa que, por defecto, los objetos de la clase Post se ordenarán en orden descendente según el campo created_on. Esto implica que los posts más recientes se mostrarán primero cuando realices consultas a la base de datos sin especificar un orden diferente.
    class Meta:
        ordering = ['-created'] 
        
    def __str__(self):
        return self.title
    
    