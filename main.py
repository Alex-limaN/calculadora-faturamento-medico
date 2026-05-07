def unimed(valor_procedimento, porte, vlr_filme, vlr_uco, aditivo): 
    filme = 21.70 * vlr_filme
    uco = 12.50 * vlr_uco
    aditivo_porc = aditivo / 100
    valor_aditivo = valor_procedimento * aditivo_porc
    valor_final = valor_procedimento + valor_aditivo + filme + uco + porte
    return valor_final

def amil(valor_procedimento, porte, vlr_filme, vlr_uco, aditivo):
    filme = 21.70 * vlr_filme
    uco = 12.50 * vlr_uco
    aditivo_porc = aditivo / 100
    valor_aditivo = valor_procedimento * aditivo_porc
    valor_final = valor_procedimento + valor_aditivo + filme + uco + porte
    return valor_final

convenio = ["Unimed", "Amil", "Bradesco", "Sulamerica", "Hapvida"].lower() #Lista de convênios disponíveis, convertida para minúsculas para facilitar a comparação com a entrada do usuário.
escolha_convenio = input("Digite o nome do convênio:").lower()
valor_procedimento = float(input("Digite o valor:")) 
porte = float(input("Digite o porte:"))
vlr_filme = float(input("Digite o filme:"))
vlr_uco = float(input("Digite o uco:"))
aditivo = float(input("Digite o aditivo:"))


print(f"O valor total do procedimento é: R$ {unimed(valor_procedimento, porte, vlr_filme, vlr_uco, aditivo):.2f}")

   