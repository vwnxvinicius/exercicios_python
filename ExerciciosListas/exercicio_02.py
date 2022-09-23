# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

vetor = [x for x in range(1, 11)]

for i in vetor:
    print(vetor[-i], end=" ")