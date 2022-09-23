'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

'''

notas = []
soma_notas = 0.0

while True:
    atleta = input("Insira o nome do atleta: ")
    if atleta == '':
        break
    else:
        # Loop para coletar as notas
        for i in range(1, 8):
            nota = float(input(f"Insira a nota da atleta: {i} de 7: "))
            notas.append(nota)
        
        print(f"\nAtleta: {atleta}\n")
        print(f"Nota: {notas[0]}")
        print(f"Nota: {notas[1]}")
        print(f"Nota: {notas[2]}")
        print(f"Nota: {notas[3]}")
        print(f"Nota: {notas[4]}")
        print(f"Nota: {notas[5]}")
        print(f"Nota: {notas[6]}")

        notas.sort()

        print("\nResultado final:")
        print(f"\nMelhor nota: {notas[-1]}")
        print(f"Pior nota: {notas[0]}")

        # Loop para conseguir a média das notas
        notas.remove(notas[-1])
        notas.remove(notas[0])
        for i in range(len(notas)):
            soma_notas += notas[i]
        media = soma_notas/len(notas)
        print(f"Média das outras notas: {'%.1f'}" %media)
        print(f"{atleta}:{'%.1f'}" %media)