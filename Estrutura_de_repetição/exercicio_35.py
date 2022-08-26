'''

Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um 
número inteiro informado pelo usuário.

'''

# Mesmo problema proposto no exercício 25
n = int(input("Insira um número inteiro:  "))
primos = []
for i in range(n + 1):
    if i % 2 == 1 and i != 2:
        primos.append(i)


print(f"Números primos: {primos}")