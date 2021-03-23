# Programa que recebe 3 números inteiros e retorna o maior e o menor número

n = int(input("Insira um número inteiro: "))
n1 = int(input("Insira outro número inteiro: "))
n2 = int(input("Insira um último número: "))

# Imprimindo o maior número
if n > n1 and n > n2:
    print(f"O maior número é {n}")
elif n1 > n and n1 > n2:
    print(f"O maior número é {n1}")
elif n2 > n and n2 > n1:
    print(f"O maior número é {n2}")

# Imprimindo o menor número
m = n
m1 = n1
m2 = n2
if m < m1 and m < m2:
    print(f"O menor número é {m}")
elif m1 < m and m1 < m2:
    print(f"O menor número é {m1}")
else:
    print(f"O menor número é {m2}")


