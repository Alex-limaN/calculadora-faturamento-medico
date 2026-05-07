from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import calcular_faturamento
from .models import CalculoHistorico

class CalculadoraView(APIView):
    def post(self, request):
        data = request.data
        
        # Mapeamos os valores manuais vindos do Vue para o formato que o services.py espera
        # Isso garante que a lógica matemática não precise ser alterada
        data['vlr_uco'] = float(data.get('valor_uco_convenio', 0))
        data['vlr_filme'] = float(data.get('valor_filme_convenio', 0))
        
        resultado = calcular_faturamento(data)
        
        if resultado is not None:
            # Salvamos no histórico apenas para registro de auditoria
            CalculoHistorico.objects.create(
                convenio_nome=data.get('convenio', 'Indefinido'),
                valor_procedimento=float(data.get('valor_procedimento', 0)),
                valor_final=resultado
            )
            return Response({"valor_final": resultado}, status=status.HTTP_200_OK)
            
        return Response({"erro": "Erro ao processar o cálculo matemático"}, status=status.HTTP_400_BAD_REQUEST)