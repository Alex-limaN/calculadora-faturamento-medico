from django.db import models

class CalculoHistorico(models.Model):
    # Alterado de ForeignKey para CharField para permitir qualquer nome de convênio, já que a tabela Convenio foi removida
    convenio_nome = models.CharField(max_length=100) 
    valor_procedimento = models.FloatField()
    valor_final = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.convenio_nome} - R$ {self.valor_final}"