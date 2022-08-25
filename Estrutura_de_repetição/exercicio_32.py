'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

n = int(input("Fatorial de: "))
x=1
fatorial = []

for i in range(n):
    x = x*(i+1)
    fatorial.append(n-i)
    valor_formatado = " . ".join(map(str,fatorial))
    print(x)
print(f"{n}! = {valor_formatado} = {x}")