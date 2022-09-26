# Faça um programa que leia 20 números inteiros e armazene os num vetor.
# Armazene os números PARES no vetor par e os números impares no vetor impar.
# No final imprima os 3 vetores.

vetor = []
par = []
impar = []

for i in range(1, 21):
    n = int(input(f"Insira um número inteiro - {i} de 20: "))
    vetor.append(n)

for i in range(len(vetor)):
    if vetor[i]%2 == 0:
        par.append(vetor[i])
    else:
        impar.append(vetor[i])

print(f"Vetor original: {vetor}")
print(f"Vetor apenas com os números pares: {par}")
print(f"Vetor apenas com números impares: {impar}")