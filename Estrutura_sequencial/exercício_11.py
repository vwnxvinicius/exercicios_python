''' 
Programa que recebe dois números inteiros e um número real e retorna:
- O produto do dobro do primeiro com metade do segundo .
- A soma do triplo do primeiro com o terceiro.
- O terceiro elevado ao cubo. 
'''
n = int(input("Insira um número inteiro: "))
n1 = int(input("Insira outro numero inteiro: "))
n2 = int(input("Insira um número real: "))
print(f"{(n*2) * (n1/2)}")
print(f"{(n*3) + n2}")
print(f"{n2**3}")
