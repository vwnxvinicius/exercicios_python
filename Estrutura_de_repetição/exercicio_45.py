'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 

Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.

    Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A

    Após concluir isto você poderia incrementar o programa permitindo que o 
    professor digite o gabarito da prova antes dos alunos usarem o programa.

'''

maior_nota = 0
menor_nota = 500
total_usuarios = 0
notas_turma = []
x = 0



# Caso o usuário desejasse escolher o gabarito
'''
gabarito = []
usuario = int(input("Quem usará o programa? Professor - 1, Aluno - 2: "))
if usuario == 1:
    for i in range(1, 11):
        alternativa = input(f"Insira a resposta da questão {i}: ").upper()
        gabarito.append(alternativa)
else:
    .....
'''



gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']


while True:
    # Loop para inserir as alternativas do aluno
    questao = 1
    pontos_aluno = 0
    for i in range(len(gabarito)):
        resposta = input(f"Insira a resposta da questão {questao}: ").upper()
        questao+=1
        if resposta == gabarito[i]:
            pontos_aluno += 1
    notas_turma.append(pontos_aluno)

    #Verificando maior e menor nota
    if pontos_aluno > maior_nota:
        maior_nota = pontos_aluno
    if pontos_aluno < menor_nota:
        menor_nota = pontos_aluno

    # Verificando se outro aluno usará o sistema
    outro_aluno = input("Outro aluno irá usar o sistema? (S) ou (N)").upper()
    if outro_aluno == 'N':
        for i in range(len(notas_turma)):
            x += notas_turma[i]
        media = x/len(notas_turma)
        print(f"Menor nota: {menor_nota}")
        print(f"Maior nota: {maior_nota}")
        print(f"Media da turma: {media}")
        break
    else:
        pass


