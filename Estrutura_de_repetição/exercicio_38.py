'''

Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:

Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. 

Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

'''
import datetime

data_e_hora_atual = datetime.datetime.now()
data = data_e_hora_atual.date()
ano_atual = data.strftime("%Y")

aumento = 1.5
tempo_recebendo = int(ano_atual) - 1997
salario_inicial = 1000+(1000*aumento/100)

for i in range(tempo_recebendo):
    salario_atual = salario_inicial+(1000*aumento/100)
    aumento = aumento*2


salario_atual_texto = f'{salario_atual:_.2f}'
salario_atual_texto = salario_atual_texto.replace('.',',').replace('_','.')
print(f"O salário atual desse funcionário é de: {salario_atual_texto}")

# Programa onde o usuário insere o salário inicial
aumento = 1.5
salario_inicial = int(input("Salário inicial: "))

for i in range(tempo_recebendo):
    salario_atual = salario_inicial+(salario_inicial*aumento/100)
    aumento = aumento*2
salario_atual_texto = f'{salario_atual:_.2f}'
salario_atual_texto = salario_atual_texto.replace('.',',').replace('_','.')
print(f"O salário atual desse funcionário é de: {salario_atual_texto}")
