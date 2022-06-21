from django.db import models

# Create your models here.
class Persona(models.Model):
    documento = models.PositiveIntegerField(max_length=30)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.correo)