'''
Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
'''

n = int(input("Insira um número inteiro:  "))
divisores = 1
for i in range(1, n+1):
    x = n % i
    if x == 0:
        divisores += 1
    if divisores > 2 and x==0:
        print(f"{n} é divisível por {i}")
if divisores == 2:
    print("É um número primo")
else:
    print("Não é um número primo")
