# api/services.py

def calcular_faturamento(dados):
    # Suas tabelas de convênios
    tabelas = {
        "unimed": {"filme": 21.70, "uco": 12.50},
        "amil": {"filme": 19.50, "uco": 10.00},
        "bradesco": {"filme": 18.00, "uco": 8.00},
        "sulamerica": {"filme": 20.00, "uco": 9.00},
        "hapvida": {"filme": 17.00, "uco": 7.00}
    }

    convenio = dados.get('convenio', '').lower()
    if convenio not in tabelas:
        return None

    vlr_filme_base = tabelas[convenio]["filme"]
    vlr_uco_base = tabelas[convenio]["uco"]
    
    # Lógica de acompanhamento e horário
    multiplicador_acomodacao = 2 if dados.get('acomodacao') == 'S' else 1
    percentual_especial = 0.3 if dados.get('horario_especial') == 'S' else 1 # 30% de acréscimo para horário especial, caso contrário, sem acréscimo
    
    # Cálculos de valores
    vlr_uco = vlr_uco_base * float(dados.get('uco_procedimento', 0))
    vlr_filme = vlr_filme_base * float(dados.get('filme_procedimento', 0))
    
    porte = float(dados.get('porte', 0))
    aditivo = float(dados.get('aditivo', 0)) / 100
    porte_final = porte + (porte * aditivo)

    # Cálculo final
    valor_soma = float(dados.get('valor_procedimento', 0)) + porte_final + vlr_uco + vlr_filme
    total = (valor_soma + (valor_soma * percentual_especial)) * multiplicador_acomodacao
    
    return round(total, 2)