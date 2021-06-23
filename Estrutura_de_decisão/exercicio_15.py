"""
Programa que recebe os valores dos lados de um triângulo e retora:
Se o triângulo é Escaleno, Equilátero ou Isósceles
"""

lado_1 = int(input("Digite o valor do primeiro lado do triângulo: "))
lado_2 = int(input("Digite o valor do segundo lado do triângulo: "))
lado_3 = int(input("Digite o valor do terceiro lado do triângulo: "))

# Verificando se é um triângulo de acordo com os valores passados
if lado_1 + lado_2 > lado_3 or lado_2 + lado_3 > lado_1 or lado_1 + lado_3 > lado_2:
    print("É um triângulo")
    if lado_1 == lado_2 == lado_3:
        print("É um triângulo Equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("É um triângulo Isósceles")
    elif lado_1 != lado_2 != lado_3:
        print("É um triângulo Escaleno")
else:
    print("Não é um triângulo")


