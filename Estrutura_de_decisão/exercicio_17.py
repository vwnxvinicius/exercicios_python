"""
Programa que recebe um número correspondente a um ano, e retorna se o ano é ou não bissexto
"""

ano = int(input("Insira um valor correspondente a um ano: "))
if ano % 4 == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")
