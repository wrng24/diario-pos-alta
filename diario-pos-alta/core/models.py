from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    diagnostico = models.CharField(max_length=200)
    data_alta = models.DateField()

    def __str__(self):
        return self.nome


class RegistroDiario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    data_registro = models.DateTimeField(auto_now_add=True)

    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    pressao_arterial = models.CharField(max_length=20)
    horas_sono = models.DecimalField(max_digits=4, decimal_places=1)

    frequencia_cardiaca = models.IntegerField(null=True, blank=True)
    frequencia_respiratoria = models.IntegerField(null=True, blank=True)
    glicemia = models.IntegerField(null=True, blank=True)

    OPCOES_FUNCIONALIDADE = [
        ('sozinho', 'Sozinho'),
        ('com_auxilio', 'Com auxílio'),
        ('nao_realizou', 'Não realizou'),
    ]

    alimentacao = models.CharField(max_length=20, choices=OPCOES_FUNCIONALIDADE)
    locomocao = models.CharField(max_length=20, choices=OPCOES_FUNCIONALIDADE)
    transferencia = models.CharField(max_length=20, choices=OPCOES_FUNCIONALIDADE)
    banho = models.CharField(max_length=20, choices=OPCOES_FUNCIONALIDADE)
    vestir_se = models.CharField(max_length=20, choices=OPCOES_FUNCIONALIDADE)

    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Registro de {self.paciente.nome}"