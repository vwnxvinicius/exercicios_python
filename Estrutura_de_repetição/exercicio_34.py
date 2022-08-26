'''

Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

'''

# Mesmo código do exercício 24
# Não entendi o porque de ser proposto o mesmo problema
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