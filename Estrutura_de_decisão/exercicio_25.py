'''

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1 - Telefonou para a vítima?
2 - Esteve no local do crime?
3 - Mora perto da vítima?
4 - Devia para a vítima?
5 - Já trabalhou com a vítima? 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


'''

from itertools import count


pergunta_1 = input("Você telefonou para a vítima? (s/n) - ")
pergunta_2 = input("Esteve no local da vítima? (s/n) - ")
pergunta_3 = input("Mora perto da vítima? (s/n) - ")
pergunta_4 = input("Devia para a vítima? (s/n) - ")
pergunta_5 = input("Já trabalhou para a vítima? (s/n) - ")

perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]

respostas_positivas = perguntas.count('s')

if respostas_positivas == 2:
    print("Suspeito")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assasino")
else:
    print("Inocente")