# Faça um programa que leia um vetor de 10 caracteres, e diga
# quantas consoantes foram lidas e imprima as consoantes.


vetor = []
for i in range(1, 11):
    caracter = input(f"Insira um caracter - {i} de {10}")
    vetor.append(caracter)

consoantes = []

for i in range(len(vetor)):
    if vetor[i] != 'a' and vetor[i] != 'e' and vetor[i] != 'i' and vetor[i] != 'o' and vetor[i] != 'u':
        consoantes.append(vetor[i])

print(f"Total de consoantes: {len(consoantes)}")
print(f"Consoantes encontradas: {consoantes}")