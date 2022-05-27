'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

n1 = int(input("Insira a primeira nota parcial do aluno: "))
n2 = int(input("Insira a segunda nota parcial do aluno: "))
n3 = int(input("Insira a terceira nota parcial do aluno: "))

m = (n1 + n2 + n3) / 2
if m >= 10:
    print("Aprovado com distinção")
elif m < 7:
    print("Reprovado")
else:
    print("Aprovado")

print(f'Nota: {m}')