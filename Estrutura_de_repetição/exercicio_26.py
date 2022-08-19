'''
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

eleitores = int(input("Insira a quantidade de eleitores: "))

print(
    "CANDIDATO 1 - DIGITE 1",
    "\nCANDIDATO 2 - DIGITE 2",
    "\nCANDIDATO 3 - DIGITE 3"
    )

for i in range(1, eleitores+1):

    voto = int(input(f"Insira aqui em quem você deseja votar ({i} de {eleitores}):  "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    else:
        voto = int(input("Insira um número válido:  "))
    
print("TOTAL DE VOTOS")
print(f"Candidato 1 - {candidato_1}")
print(f"Candidato 2 - {candidato_2}")
print(f"Candidato 3 - {candidato_3}")
