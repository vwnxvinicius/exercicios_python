from math import sqrt
"""
Programa que calcula as raízes de uma equação de segundo grau, sendo a fórmula: ax2 + bx + c;
- Se o usuário informar A como sendo 0, o programa será encerrado por não ser mais uma equação do segundo grau;
- Se o delta calculado for negativo, a equação não possui raizes reais. O programa informará ao usuário e se encerrará;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; o programa informará ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais; o programa as informará ao usuário;
"""

a = float(input("Digite o valor de A na equação: "))
if a == 0:
    print("O valor de A informado é 0, portanto não é uma equação de segundo grau "
          "o programa será encerrado")
    quit()
b = float(input("Digite o valor de B na equação: "))
c = float(input("Digite o valor de C na equação: "))

delta = (b ** 2) - (4 * a * c)
raiz_p = (-b + sqrt(delta)) / (2 * a)
raiz_n = (-b - sqrt(delta)) / (2 * a)
if delta < 0:
    print("A equação não possui raizes reais, o programa será encerrado!")
elif delta == 0:
    print(f"O programa possui apenas uma raiz real: {raiz_p}")
elif delta > 0:
    print(f"O programa possui duas raízes reais: {raiz_p}, {raiz_n}")
