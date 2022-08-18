'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
pessoas = int(input("Quantas pessoas há na turma?  "))
idades = []
x = 0

for i in range(1, pessoas+1):
    idade = int(input(f"Cada pessoa na turma insira sua idade ({i} de {pessoas}):  "))
    idades.append(idade)

for i in range(len(idades)):
    x += idades[i]

media = x/pessoas
if media <= 25:
    print("Conforme a média de idade da turma, a turma é considerada jovem")
elif media >= 26 and media < 60:
    print("Conforme a média de idade da turma, a turma é considerada adulta")
else:
    print("Conforme a média de idade da turma, a turma é considerada idosa")
