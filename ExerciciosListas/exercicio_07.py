# Faça um programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

vetor = []
soma = 0
multiplicacao = 1

for i in range(1, 6):
    n = int(input(f"Insira um número inteiro - {i} de 5: "))
    vetor.append(n)


for i in range(len(vetor)):
    soma += vetor[i]
    multiplicacao *= vetor[i]

print(f"Vetor com 5 números: {vetor}")
print(f"Soma dos números do vetor: {soma}")
print(f"Multiplicação dos números do vetor: {multiplicacao}")
