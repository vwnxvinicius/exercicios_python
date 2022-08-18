'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

n = int(input("Insira um número inteiro:  "))
divisores = 0
for i in range(1, n+1):
    x = n % i
    if x == 0:
        divisores += 1
if divisores == 2:
    print("É um número primo")
else:
    print("Não é um número primo")
