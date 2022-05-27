"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
"""

n = int(input("Insira um número inteiro menor que 1000: "))
unidades = n % 10
dezenas = (((n - unidades) / 10) % 10)
centenas = n // 100
if unidades == 1:
    unidades = '1 Unidade'
elif unidades > 1:
    unidades = f'{unidades} Unidades'

if dezenas == 1:
    dezenas = '1 Dezena'
elif dezenas > 1:
    dezenas = f'{dezenas} Dezenas'

if centenas == 1:
    centenas == '1 Centena'
elif centenas > 1:
    centenas == f'{centenas} Centenas'

print(centenas, ',', dezenas, ' e', unidades)



