'''
Faça um programa que leia 5 números e informe o maior número.
'''
x = 1
lista = []
while x <= 5:
    n = int((input(f"Insira 1 número de 5  ({x}):")))
    lista.append(n)
    x+=1
lista_ordenada = sorted(lista)
print(f"O maior número é: {lista_ordenada[-1:]}")