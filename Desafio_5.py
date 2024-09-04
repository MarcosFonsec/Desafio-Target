def inverter_string(string):
    string_invertida = ""  # Armazena o resultado da string invertida

    # Loop for para iterar sobre os indices da string original, começando do último índice e indo até o primeiro, com um passo de -1
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida  # Retorna a string_invertida


# Fluxo de execução
string_original = input("Digite a string que deseja inverter: ")
string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
