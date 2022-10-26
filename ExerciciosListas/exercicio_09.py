# Faça um programa que leia um vetor A com 10 números inteiros
# Mostre a soma, a multiplicação e os números

a = []
soma  = 0
multiplicacao = 1


for i in range(1, 11):
    n = int(input(f"Insira um número - {i} e 10: "))
    a.append(n)

for i in range(len(a)):
    soma += a[i]
    multiplicacao *= a[i]

print(f"Números escolhidos: {a}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")
