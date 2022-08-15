'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
lista = []
pares = 0
impares = 0

for i in range(1, 11):
    x = int(input(f"Insira um número inteiro: ({i} de 10)  "))
    lista.append(x)
print(lista)

for i in lista:
    if lista[i] % 2 == 0:
        pares+=1
    else:
        impares+=1
print(f"Número pares: {pares}  ")
print(f"Número ímpares: {impares}")