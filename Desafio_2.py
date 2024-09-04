def fibonacci(n):
    a, b = 0, 1  # Início da sequência Fibonacci 0, 1
    while a <= n:  # Loop continuará a ser executado enquanto a <= n
        if a == n:  # Se a == n, indica que o número pertence à sequência Fibonacci
            return True
        a, b = b, a + b  # Atualiza os valores de a e b para gerar o próximo número da sequência
    return False  # Se a > n, o número não pertence à sequência Fibonacci


# Pede ao usuário que insira um número a ser verificado
numero = int(input("Informe um número: "))

if fibonacci(numero):  # Se a função fibonacci retorna True, o número pertence à sequência
    print(f"O número {numero} pertence à sequência Fibonacci.")
else:  # Se a função fibonacci retorna False, o número não pertence à sequência
    print(f"O número {numero} não pertence à sequência Fibonacci.")
