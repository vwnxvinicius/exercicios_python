'''
Faça um programa que receba dois 
números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
x = int(input("Insira um número inteiro: "))
y = int(input("Insira outro número inteiro: "))

if x < y:
    for i in range(x,y, 1):
        print(i)
else:
    for i in range(y,x, 1):
        print(i)