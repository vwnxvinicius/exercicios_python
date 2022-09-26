# Faça um programa que leia 4 notas, leia as notas e mostre a média
notas = []
soma = 0

for i in range(1, 5):
    nota = float(input(f"Insira a nota do aluno - {i} de 4: "))
    notas.append(nota)

for i in range(len(notas)):
    soma += notas[i]

print(soma/len(notas))