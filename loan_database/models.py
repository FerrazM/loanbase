from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, date


class Cliente(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(
        max_length=16, help_text='Insira o telefone com DDD', null=True, blank=True)
    endereco = models.TextField(
        max_length=300, null=True, blank=True, verbose_name='Endereço')
    valor = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor R$', name='valor')
    juros = models.CharField(max_length=22, verbose_name='juros %',
                             help_text='Insira a porcentagem de juros')
    parcelas = models.IntegerField(default=1, blank=True, null=True)
    parcelas_pagas = models.IntegerField(default=0, blank=True, null=True)
    parcelas_atrasadas = models.IntegerField(
        default=0, null=True, blank=True, verbose_name='Parcelas em Atraso')
    pagamento_mensal = models.DecimalField(
        max_digits=22, decimal_places=2, verbose_name='Valor de pagamento mensal',
        help_text='Insira o valor dos juros mensais', name='juros_mes')
    data_emprestimo = models.DateField(
        blank=True, null=True, verbose_name='Data do empréstimo')
    vencimento_mensal = models.DateField(verbose_name='Vence:',
                                         blank=True, null=True)
    observacao = models.TextField(
        max_length=300, null=True, blank=True, verbose_name='Observação')
    mensalidade_paga = models.BooleanField(
        default=False, verbose_name='Mensalidade Paga', name='checkbox1')
    divida_total_paga = models.BooleanField(
        default=False, verbose_name='Dívida Total Paga', name='checkbox2')

    def save(self, *args, **kwargs):
        # Verifica se a data de vencimento é menor ou igual à data atual
        if self.vencimento_mensal and self.vencimento_mensal <= date.today():
            self.checkbox1 = False

        super().save(*args, **kwargs)

    @property
    def parcelas_restantes(self):
        return self.parcelas - self.parcelas_pagas

    def parcelas_pagas_string(self):
        return f"{self.parcelas_pagas}/{self.parcelas} parcelas pagas"
