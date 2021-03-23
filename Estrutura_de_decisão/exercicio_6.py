# Programa que recebe 3 números inteiros e retorna o maior deles

n = int(input("Insira um número inteiro: "))
n1 = int(input("Insira outro número inteiro: "))
n2 = int(input("Insira um último número: "))

if n > n1 and n > n2:
    print(f"O maior número é {n}")
elif n1 > n and n1 > n2:
    print(f"O maior número é {n1}")
else:
    print(f"O maior número é {n2}")
