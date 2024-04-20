from django.db import models
from django.contrib.auth.models import User

set
DJANGO_SETTINGS_MODULE="Appcoder.settings"

# Create your models here.



class Curso (models.Model):  #clase curso hereda de la clase Model que es la clase padre y le da un monton de funcionalidad
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()
    def __str__(self): 
        return f"Nombre:{self.nombre} Camada:{self.camada}"

#

class Alumnos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido}"

#

class Profesores(models.Model):
    nombre= models.CharField(max_length=30)
    materia=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre:{self.nombre} Materia:{self.materia}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)

    def __str__(self):
        return f"user:{self.user} image:{self.imagen}"

