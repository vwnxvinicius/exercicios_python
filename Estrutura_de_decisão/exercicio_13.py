"""Programa que recebe um número do usuário e retorna um dia da semana correspondente ao número
Retornará valor inváçido caso o número seja diferente de: 1, 2, 3, 4, 5, 6, 7
"""
n = int(input("Digite um número de 1 a 7: "))
if n == 1:
    print("Domingo")
elif n == 2:
    print("Segunda")
elif n == 3:
    print("Terça")
elif n == 4:
    print("Quarta")
elif n == 5:
    print("Quinta")
elif n == 6:
    print("Sexta")
elif n == 7:
    print("Sábado")
else:
    print("Valor inválido")

