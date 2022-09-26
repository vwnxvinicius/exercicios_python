# Faça um programa que peça as quatro notas de 10 alunos,
# Calcule e armazene a média de cada um em um vetor
# Imprima o número de alunos com média maior ou igual a 7.0

media = []
alunos_na_media = 0

for i in range(1, 10):
    soma = 0
    print(f"Insira abaixo as notas do aluno - {i} de 10")
    for i in range(1, 5):
        nota = float(input(f"Insira a nota - {i} de 4: "))
        soma += nota
    media.append(soma/4)

for i in range(len(media)):
    if media[i] >= 7:
        alunos_na_media += 1
    else:
        pass

print(f"Total de alunos na média: {alunos_na_media}")