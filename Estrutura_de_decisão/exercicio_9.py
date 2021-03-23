# Programa que recebe 3 números e os retorna em ordem decrescente

n = int(input("Digite um número inteiro: "))
n1 = int(input("Digite mais um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n <= n1 and n1 <= n2:
    print(f"A ordem decrescente é {n2}, {n1}, {n}")
elif n1 <= n and n <= n2:
    print(f"A ordem decrescente é {n2}, {n}, {n1}")
elif n2 <= n and n <= n1:
    print(f"A ordem decrescente é {n1}, {n}, {n2}")
elif n2 <= n1 and n1 <= n:
    print(f"A ordem decrescente é {n}, {n1}, {n2}")
elif n <= 2 and n2 <= n1:
    print(f"A ordem decrescente é {n1}, {n2}, {n}")
elif n1 <= n2 and n2 <= n:
    print(f"A ordem decrescente é {n}, {n2}, {n1}")
