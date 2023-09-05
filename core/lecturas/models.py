from django.conf import settings
from django.db import models

class Medidor(models.Model):
    nombres = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    suministro = models.CharField(max_length=50)
    nserie = models.CharField(max_length=50)
    marcaMedidor = models.CharField(max_length=50)
    tarifa = models.CharField(max_length=20)
    fases = models.IntegerField(default=0)
    sed = models.CharField(max_length=100)


    def __str__(self):
        return self.suministro

class Lectura(models.Model):
    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    suministro = models.CharField(max_length=50)
    fecha_lectura = models.DateTimeField(auto_now_add=True)
    fotografia = models.ImageField(upload_to='images/', null=True, blank=True)
    valor_lectura = models.FloatField()

    def __str__(self):
        return f' {self.suministro} - {self.fecha_lectura}'

