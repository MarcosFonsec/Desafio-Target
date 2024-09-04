def calcular_percentuais():
    faturamento_estados = {  # Dicionário com os valores de faturamento de cada estado
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    # Calcula a soma de todos os valores para obter o faturamento total
    faturamento_total = sum(faturamento_estados.values())

    percentuais = [(estado, (valor / faturamento_total) * 100)
                   # Calculo do porcentual
                   for estado, valor in faturamento_estados.items()]

    for estado, percentual in percentuais:  # Calculo o percentual de cada estado em relação ao total
        print(f"{estado}: {percentual:.2f}%")


# Execução
calcular_percentuais()
