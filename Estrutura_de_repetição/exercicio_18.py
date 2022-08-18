'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
n = int(input("Insira um número inteiro: "))
operacao = int(input("Deseja continuar adicionando números? 1-SIM 2-NÃO:  "))
x = 0

lista = [n]
while operacao == 1:
    n = int(input("Insira um número inteiro: "))
    operacao = int(input("Deseja continuar adicionando números? 1-SIM 2-NÃO:  "))
    lista.append(n)

lista.sort()
for i in range(len(lista)):
    x += lista[i]

print(f"Menor número: {lista[0]}")
print(f"Maior número: {lista[-1]}")
print(f"Soma de todos os números: {x}")