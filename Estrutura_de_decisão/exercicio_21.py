'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a 
valor do saque e depois informar quantas notas de cada valor 
serão fornecidas. As notas disponíveis serão
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 
reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
n = int(input("Insira o valor do saque (mínimo 10 e máximo 600): "))

cem = 0
cinq = 0
dez = 0
cinco = 0
um = 0

if n % 100 == 0:
    cem = n // 100
elif n % 50 == 0:
    cinq = n // 50
elif n % 10 == 0:
    dez = n // 10
elif n % 5 == 0 :
    cinco = n // 5
elif n % 1 == 0:
    um = n // 1
print(f"Para sacar {n}, você precisa de {cem} notas de cem, {cinq} de cinquenta, {dez} de dez, {cinco} de cinco e {um} de um")
