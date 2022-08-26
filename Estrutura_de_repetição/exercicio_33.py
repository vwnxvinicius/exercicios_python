'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a 
maior temperaturas informadas, bem como a média das temperaturas.

'''

print("Não insira nada para encerrar o programa")
temp = input("Insira a temperatura(C°): ")
# Valor default para não causar erro ao não inserir nenhuma temperatura
str_temperaturas = [0]
if temp != '':
    str_temperaturas = [temp]
temperaturas = []
soma = 0

# Coletando as temperaturas e armazenando em uma lista
while temp != '':
    temp = input("Insira a temperatura(C°): ")
    if temp == '':
        break
    str_temperaturas.append(temp)


# Transformando os valores em inteiros
for i in range(len(str_temperaturas)):
    temperaturas.append(int(str_temperaturas[i]))


# Calculando a média
for i in range(len(temperaturas)):
    soma += temperaturas[i]

temperaturas.sort()
media = soma/len(temperaturas)
maior = temperaturas[-1]
menor = temperaturas[0]

print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Media das temperaturas: {media}")