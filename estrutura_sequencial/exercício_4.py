# Programa que recebe 4 notas bimestrais de um aluno e imprime a média.

nota_1 = float(input("Digite a primeira nota bimestral do aluno: "))
nota_2 = float(input("Digite a segunda nota bimestral do aluno: "))
nota_3 = float(input("Digite a terceira nota bimestral do aluno: "))
nota_4 = float(input("Digite a quarta nota bimestral do aluno: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) /2
print(f"A média das 4 notas bimestrais do aluno é {media}")