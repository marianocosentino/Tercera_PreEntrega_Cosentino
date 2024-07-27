from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.titulo

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    cursos = models.ManyToManyField(Curso, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"