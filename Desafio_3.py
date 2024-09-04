import json

# Função para que o usuário possa digitar a quantidade de dias do mês e o faturamento diário.
# def salvar_faturamento():
# Solicitar o número de dias do mês (28, 30, ou 31)
#    numero_dias = int(input("Quantos dias o mês tem? "))

#    faturamento_diario = []

# Solicitar o faturamento para cada dia
#    for dia in range(1, numero_dias + 1):
#        valor = float(input(f"Digite o valor do faturamento para o dia {dia}: "))
#        faturamento_diario.append({"dia": dia, "valor": valor})

# Salva em um arquivo json
#    with open('faturamento.json', 'w') as file:
#        json.dump(faturamento_diario, file)
#    print("Faturamento salvo com sucesso!")


def salvar_faturamento():  # Função que cria uma lista de dicionários que representam o faturamento mensal
    faturamento_diario = [
        {"dia": 1, "valor": 100},
        {"dia": 2, "valor": 120},
        {"dia": 3, "valor": 110},
        {"dia": 4, "valor": 200},
        {"dia": 5, "valor": 250},
        {"dia": 6, "valor": 100},
        {"dia": 7, "valor": 0},
        {"dia": 8, "valor": 140},
        {"dia": 9, "valor": 140},
        {"dia": 10, "valor": 120},
        {"dia": 11, "valor": 210},
        {"dia": 12, "valor": 280},
        {"dia": 13, "valor": 90},
        {"dia": 14, "valor": 0},
        {"dia": 15, "valor": 120},
        {"dia": 16, "valor": 170},
        {"dia": 17, "valor": 130},
        {"dia": 18, "valor": 230},
        {"dia": 19, "valor": 290},
        {"dia": 20, "valor": 160},
        {"dia": 21, "valor": 0},
        {"dia": 22, "valor": 120},
        {"dia": 23, "valor": 130},
        {"dia": 24, "valor": 140},
        {"dia": 25, "valor": 250},
        {"dia": 26, "valor": 350},
        {"dia": 27, "valor": 120},
        {"dia": 28, "valor": 0},
        {"dia": 29, "valor": 90},
        {"dia": 30, "valor": 150},
        {"dia": 31, "valor": 120},
    ]

    with open("faturamento.json", "w") as file:
        # Salva a lista de faturamento em um arquivo json
        json.dump(faturamento_diario, file)


def ler_faturamento():  # Lê os dados do arquivo json
    with open("faturamento.json", "r") as file:
        return json.load(file)  # Carrega os dados de faturamento


def processar_faturamento(faturamento):  # Filtrar dias com faturamento > 0
    dias_com_faturamento = [dia["valor"]
                            for dia in faturamento if dia["valor"] > 0]

    # Menor e maior valor de faturamento
    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)

    # Média de faturamento
    media = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contar dias com faturamento acima da média
    dias_acima_da_media = len(
        [valor for valor in dias_com_faturamento if valor > media])

    return menor_valor, maior_valor, media, dias_acima_da_media


def resultados(menor_valor, maior_valor, media, dias_acima_da_media):
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Média de faturamento: {media:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

    # Fluxo de execução
salvar_faturamento()
faturamento = ler_faturamento()
menor, maior, media, dias_acima = processar_faturamento(faturamento)
resultados(menor, maior, media, dias_acima)
