# Programa que recebe duas notas parciais de um aluno e retorna com base na média
# Se o aluno foi aprovado caso a média seja maior que 7
# Se ele foi reprovado caso a média seja menor que 7
# Ou se ele foi aprovado com distinção caso a média seja igua a 10

n = float(input("Insira a nota parcial do aluno: "))
n2 = float(input("Insira a segunda nota parcial do aluno: "))
m = (n + n2) / 2
if m < 7:
    print(f'O aluno foi reprovado, nota final: {m}')
elif m == 10:
    print(f'O aluno foi aprovad0 com distinção!!!! Nota final: {m}')
else:
    print(f'O aluno foi aprovado, nota final: {m}')
