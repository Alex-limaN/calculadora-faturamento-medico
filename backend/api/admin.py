from django.contrib import admin
from .models import CalculoHistorico

# Como não existe mais a tabela Convenio, registramos apenas o Historico
admin.site.register(CalculoHistorico)