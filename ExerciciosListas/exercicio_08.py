# Faça um programa que leia a idade e altura de 5 pessoas
# Armazene os valores no seu respectivo vetor 
# Imprima a idade e a altura na ordem inversa de ordem lida


idades = []
alturas = []


for i in range(1, 6):
    idade = int(input(f"Insira a idade - {i} de 5: "))
    altura = float(input(f"Insira a aultura - {i} de 5: "))
    idades.append(idade)
    alturas.append(altura)


idades.reverse()
alturas.reverse()

print(idades)
print(alturas)