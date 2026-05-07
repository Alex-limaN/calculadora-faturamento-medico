from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

unimed ={"filme": 21.70, "uco": 12.50}
amil = {"filme": 19.50, "uco": 10.00}
bradesco = {"filme": 18.00, "uco": 8.00}
sulamerica = {"filme": 20.00, "uco": 9.00}
hapvida = {"filme": 17.00, "uco": 7.00}

escolha_convenio = input("Digite o nome do convênio: ").lower() #Solicita ao usuário que digite o nome do convênio e converte a entrada para minúscula para facilitar a comparação.
while escolha_convenio not in ["unimed", "amil", "bradesco", "sulamerica", "hapvida"]: #Verifica se a escolha do convênio está entre as opções válidas. Se não estiver, exibe uma mensagem de erro e solicita novamente a entrada.
    print("Convênio inválido. Por favor, escolha um convênio válido 'unimed', 'amil', 'bradesco', 'sulamerica', 'hapvida'.")
    escolha_convenio = input("Digite o nome do convênio: ").lower()
acomodacao = input("A acomodação é apartamento? S ou N: ").lower()
if acomodacao == "s":
    acomodacao = 2
else:
    acomodacao = 1
while acomodacao not in ["s", "n"]: #Verifica se a entrada para acomodação é válida. Se não for, exibe uma mensagem de erro e solicita novamente a entrada.
    print("Entrada inválida. Por favor, responda com 'S' para sim ou 'N' para não.")
    acomodacao = input("A acomodação é apartamento? S ou N: ").lower()
horario_especial = input("O procedimento é em horário especial? S ou N: ").lower()
while horario_especial not in ["s", "n"]: #Verifica se a entrada para horário especial é válida. Se não for, exibe uma mensagem de erro e solicita novamente a entrada.
    print("Entrada inválida. Por favor, responda com 'S' para sim ou 'N' para não.")
    horario_especial = input("O procedimento é em horário especial? S ou N: ").lower()
if horario_especial == "s":
    horario_especial = 0.3
else:
    horario_especial = 1
if escolha_convenio == "unimed":
    vlr_filme = unimed["filme"]
    vlr_uco = unimed["uco"]
elif escolha_convenio == "amil":
    vlr_filme = amil["filme"]
    vlr_uco = amil["uco"]
elif escolha_convenio == "bradesco":
    vlr_filme = bradesco["filme"]
    vlr_uco = bradesco["uco"]
elif escolha_convenio == "sulamerica":
    vlr_filme = sulamerica["filme"]
    vlr_uco = sulamerica["uco"]
elif escolha_convenio == "hapvida":
    vlr_filme = hapvida["filme"]
    vlr_uco = hapvida["uco"]
else:
    escolha_convenio not in ["unimed", "amil", "bradesco", "sulamerica", "hapvida"] #Verifica se a escolha do convênio não está entre as opções válidas. Se for o caso, exibe uma mensagem de erro.
    print("Convênio inválido. Por favor, escolha um convênio válido 'unimed', 'amil', 'bradesco', 'sulamerica', 'hapvida'.")
valor_procedimento = float(input("Digite o valor do procedimento: "))
aditivo = float(input("Digite o valor do aditivo: "))
if aditivo <= 0:#Verifica se o valor do aditivo é menor ou igual a zero. Se for, atribui o valor 1 ao aditivo para evitar que ele seja subtraído do valor final.
    aditivo = 1
else:
    aditivo = aditivo / 100 #Converte o valor do aditivo para porcentagem, dividindo-o por 100.
porte = float(input("Digite o valor do porte: "))
uco_procedimento = float(input("Digite o valor do uco do procedimento: "))
filme_procedimento = float(input("Digite o valor do filme do procedimento: "))
vlr_uco = vlr_uco * uco_procedimento
vlr_filme = vlr_filme * filme_procedimento
porte = porte + (porte * aditivo)


def calcular_valor_final(valor_procedimento, porte, vlr_uco, vlr_filme, acomodacao): #função com parâmetros para calcular o valor final do procedimento, somando o valor do procedimento, o aditivo, o porte, o valor do uco e o valor do filme.
    valor_soma = valor_procedimento + porte + vlr_uco + vlr_filme
    valor_soma = valor_soma + (valor_soma * horario_especial) #Adiciona o valor do horário especial ao valor total, multiplicando o valor soma pelo percentual do horário especial e somando ao valor soma.
    return valor_soma * acomodacao # o return retorna o valor calculado para a variável valor_final, que é exibida ao usuário com duas casas decimais.


valor_final = calcular_valor_final(valor_procedimento, porte, vlr_uco, vlr_filme, acomodacao)
print(f"O valor final do procedimento é: R$ {valor_final:.2f}")