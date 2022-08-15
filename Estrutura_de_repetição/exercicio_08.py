'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
x = 1
lista = []
while x <= 5:
    n = int((input(f"Insira 1 número de 5  ({x}):")))
    lista.append(n)
    x+=1
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma)
