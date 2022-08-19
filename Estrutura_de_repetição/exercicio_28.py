'''
Faça um programa que calcule o valor total investido por um 
colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

cds = int(input("Insira a quantidade de CD'S comprados: "))
precos = []
valor_total = 0

for i in range(1, cds+1):
    preco = float(input(f"Insira quanto pagou no cd {i}:"))
    precos.append(preco)
    valor_total += preco

soma = 0
for i in range(cds):
    soma += precos[i]
media = soma/cds

print(f"O valor total pago foi de: {valor_total}")
print(f"Ele comprou {cds} cds e o valor médio pago para cada um foi de {media}")