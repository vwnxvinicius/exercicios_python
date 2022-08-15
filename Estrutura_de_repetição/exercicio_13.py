'''
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''

base = int(input("Insira uma base: "))
expoente = int(input("Insira um expoente: "))
resultado=0
for i in range(expoente):
    resultado += base*base
    print(resultado)