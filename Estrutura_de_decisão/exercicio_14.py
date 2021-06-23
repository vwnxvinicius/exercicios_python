"""
Programa que recebe duas notas parciais de um aluno e retorna:
O conceito da nota: A, B ,C ,D ou E
Se o Aluno foi reprovado ou aprovado:
Entre 9.0 e 10.0        A   - Aprovado
Entre 7.5 e 9.0         B   - Aprovado
Entre 6.0 e 7.5         C   - Aprovado
Entre 4.0 e 6.0         D   - Reprovado
Entre 4.0 e zero        E   - Reprovado
"""

nota_1 = float(input("Digite sua primeira nota parcial: "))
nota_2 = float(input("Digite sua Segunda nota parcial: "))
media = (nota_1 + nota_2) / 2
print(media)
if  media >= 9 and media <= 10:
    print("Conceito: A - Aprovado\n"
          f"Média: {media}, Notas: {nota_1}, {nota_2}")
elif media >= 7.5 and media <= 9:
    print("Conceito: B - Aprovado\n"
          f"Média: {media}, Notas: {nota_1}, {nota_2}")
elif media >= 6 and media <= 7.5:
    print("Conceito: C - Aprovado\n"
          f"Média: {media}, Notas: {nota_1}, {nota_2}")
elif media >= 4 and media <= 6:
    print("Conceito: D - Reprovado\n"
          f"Média: {media}, Notas: {nota_1}, {nota_2}")
elif media <= 4:
    print("Conceito: E - Reprovado\n"
          f"Média: {media}, Notas: {nota_1}, {nota_2}")
