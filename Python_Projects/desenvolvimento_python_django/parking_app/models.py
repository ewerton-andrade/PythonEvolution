from django.db import models
from datetime import datetime

# Create your models here.
class Carro(models.Model):
    placa_carro = models.CharField(max_length=9)
    modelo_carro = models.CharField(max_length=100)
    cor_do_carro = models.CharField(max_length=100)
    entrada = models.DateTimeField(default = datetime.now)
    saida = models.DateTimeField(default= datetime.now)
    parking_time = models.DurationField()
    preco = models.FloatField()