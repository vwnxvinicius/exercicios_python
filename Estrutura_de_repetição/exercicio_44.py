'''
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

    1 , 2, 3, 4  - Votos para os respectivos candidatos 
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. 
'''

print("Para encerrar as votações digite: 0")
print(
    "1 - A",
    "\n2 - B",
    "\n3 - C",
    "\n4 - D",
    "\n5 - NULO"
    "\n6 - BRANCO"
)

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto_nulo = 0
voto_branco = 0
total_votos = 0

while True:
    voto = int(input("Insira aqui seu voto: "))
    if voto == 0:
        break

    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1


    total_votos += 1

print("RESULTADO DAS ELEIÇÕES")
print(f"Total de votos: {total_votos}")
print(f"Candidato A: {candidato_1}")
print(f"Candidato B: {candidato_2}")
print(f"Candidato C: {candidato_3}")
print(f"Candidato D: {candidato_4}")
print(f"Votos nulos: {voto_nulo}")
print(f"Votos em branco: {voto_branco}\n")

print("As porcentagens são em cima do valor total de votos")
print(f"Porcentagem de votos nulo: {(voto_nulo * total_votos) /100}")
print(f"Porcentagem de votos em branco: {(voto_branco * total_votos) /100}")