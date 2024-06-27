from django.db import models
from datetime import datetime, timedelta

SERVICOS = {
  'Manuntenção': 'Manuntenção',
  'Limpeza': 'Limpeza',
  'Limpeza preventiva': 'Limpeza preventiva',
}

class Client(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField(max_length=200)
  servico = models.CharField(max_length=200, choices=SERVICOS)
  data_servico = models.DateField(max_length=200)
  data_servico_futuro = models.DateField(max_length=200)

  def __str__(self):
    return self.nome