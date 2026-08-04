from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import calcular_faturamento
from .models import CalculoHistorico
import traceback

class CalculadoraView(APIView):
    def post(self, request):
        try:
            dados = request.data or {}

            # Função auxiliar para conversão segura de tipos
            def converte(val):
                try:
                    return float(val)
                except (ValueError, TypeError):
                    return 0.0

            # 1. Pega os valores vindos do Vue (com padrão 0 se vier vazio ou None)
            vlr_proc = converte(dados.get('valor_procedimento'))
            porte = converte(dados.get('porte'))
            vlr_uco = converte(dados.get('valor_uco_convenio'))
            uco_proc = converte(dados.get('uco_procedimento'))
            vlr_filme = converte(dados.get('valor_filme_convenio'))
            filme_proc = converte(dados.get('filme_procedimento'))
            aditivo = converte(dados.get('aditivo'))

            # 2. Checkboxes ('S' ou 'N')
            tem_acomodacao = dados.get('acomodacao') == 'S'
            tem_horario = dados.get('horario_especial') == 'S'

            # 3. Lógica do Cálculo
            total_uco = vlr_uco * uco_proc
            total_filme = vlr_filme * filme_proc
            
            valor_final = vlr_proc + porte + total_uco + total_filme

            if aditivo > 0:
                valor_final += valor_final * (aditivo / 100)

            if tem_acomodacao:
                valor_final *= 1.2
            if tem_horario:
                valor_final *= 1.3

            return Response({'valor_final': round(valor_final, 2)}, status=status.HTTP_200_OK)

        except Exception as e:
            # IMPRIME O ERRO REAL NO LOG DO RENDER
            print("=" * 40)
            print("ERRO DETECTADO NA CALCULADORA:")
            traceback.print_exc()
            print("=" * 40)
            
            # Retorna o motivo em formato JSON para a Vercel não dar 500 genérico
            return Response({'erro_backend': str(e)}, status=status.HTTP_400_BAD_REQUEST)