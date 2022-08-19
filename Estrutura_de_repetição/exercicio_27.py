'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''
turmas = []
turma = int(input("Insira a quantidade de turmas: "))
for i in range(1, turma+1):
    alunos = int(input(f"Insira a quantidade de alunos da turma {i}: "))
    turmas.append(alunos)

soma = 0
for i in range(turma):
    soma += turmas[i]
media = soma/turma
print(f"A média de alunos por turma é de :{media}")