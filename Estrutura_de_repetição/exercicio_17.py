'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
n = int(input("Insira um número para calcular o fatorial: "))
x=1
for i in range(n):
    x = x*(i+1)
print(x)