'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

Progama anterior: 
    Faça um programa que, dado um conjunto de N números, 
    determine o menor valor, o maior valor e a soma dos valores.
'''


x = 0
lista = []
while True:
    n = int(input("Insira um número inteiro: "))
    if n < 0 or n > 1000:
        n = int(input("O número precisa estar entre 0 e 1000: "))
    operacao = int(input("Deseja continuar adicionando números? 1-SIM 2-NÃO:  "))
    if operacao == 2:
        break
    lista.append(n)

lista.sort()
for i in range(len(lista)):
    x += lista[i]

print(f"Menor número: {lista[0]}")
print(f"Maior número: {lista[-1]}")
print(f"Soma de todos os números: {x}")